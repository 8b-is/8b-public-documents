#!/usr/bin/env python3
"""Measure exact local codec round trips; never replace canonical library files.

Uses Python's gzip as the always-available baseline. Optional executables are
explicit arguments. No service, LLM, credentials, or network calls are used.
Reports file names and repository commits, never workstation paths.
"""
import argparse
import collections
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "library-tools"
PAPERS = ("unknown-not-dontcare", "vocabulary-to-kernel", "fixed-point-essay")
QUALIFIERS = ("proposed", "not yet verified", "unknown", "don't-care", "not", "implementation", "tests")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, **kwargs):
    return subprocess.run([str(x) for x in command], check=True, capture_output=True, timeout=120, **kwargs).stdout


def revision(repository):
    if not repository:
        return None
    return {"commit": run(["git", "-C", repository, "rev-parse", "HEAD"]).decode().strip(),
            "working_tree_clean": not bool(run(["git", "-C", repository, "status", "--porcelain"]).strip())}


def compare(source, candidate):
    result = {"output_sha256": sha(candidate), "byte_identical": source == candidate}
    try:
        original, output = source.decode("utf-8"), candidate.decode("utf-8")
    except UnicodeDecodeError:
        return result
    result["same_after_whitespace_normalization"] = " ".join(original.split()) == " ".join(output.split())
    counts = {}
    for term in QUALIFIERS:
        before, after = original.lower().count(term), output.lower().count(term)
        if before or after:
            counts[term] = {"before": before, "after": after}
    result["qualifier_substring_counts"] = counts
    # Exact textual spans are a diagnostic, not a semantic preservation metric.
    spans = re.findall(r"\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$\$[\s\S]*?\$\$|\\(?:cite|ref)\{[^}]+\}", original)
    required, observed = collections.Counter(spans), collections.Counter()
    for span in required:
        observed[span] = output.count(span)
    result["math_and_reference_spans"] = {
        "before": len(spans),
        "retained_verbatim": sum(min(count, observed[span]) for span, count in required.items()),
    }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--marqant-bin", type=Path)
    parser.add_argument("--marqant-repo", type=Path)
    parser.add_argument("--kompress-repo", type=Path)
    parser.add_argument("--bun", type=Path)
    parser.add_argument("--output", type=Path, default=TOOLS / "results.json")
    args = parser.parse_args()
    if bool(args.marqant_bin) != bool(args.marqant_repo):
        parser.error("--marqant-bin and --marqant-repo must be supplied together")
    if bool(args.bun) != bool(args.kompress_repo):
        parser.error("--bun and --kompress-repo must be supplied together")
    files = [ROOT / "library" / "sources" / name / f"{name}.{ext}"
             for name in PAPERS for ext in ("tex", "pdf")]
    files += [ROOT / "library" / "readers" / f"{name}.md" for name in PAPERS
              if (ROOT / "library" / "readers" / f"{name}.md").exists()]
    files += [TOOLS / "fixtures" / "fidelity.md"]
    report = {
        "schema_version": 1,
        "scope": "Three revised papers and a synthetic fidelity fixture; optional generated Markdown readers when present.",
        "claims": "Byte measurements and exact comparisons only. Qualifier counts are diagnostics, not proof of semantic equivalence. No token or retrieval-quality benchmark was run.",
        "tools": {"gzip": {"level": 9, "mtime": 0},
                  "marqant": revision(args.marqant_repo) if args.marqant_bin else {"status": "not_run"},
                  "kompress": revision(args.kompress_repo) if args.bun else {"status": "not_run"}},
        "results": [],
    }
    if args.bun:
        report["tools"]["kompress"]["bun_version"] = run([args.bun, "--version"]).decode().strip()
        report["tools"]["kompress"]["entrypoint"] = "src/rewriter.ts compressMessage; pure local rewriter, no pruning/circulator or hosted API"
    if args.marqant_bin:
        report["tools"]["marqant"]["binary_sha256"] = sha(args.marqant_bin.read_bytes())
        report["tools"]["marqant"]["timestamp_override"] = "MARQANT_TEST_TS=0"
        report["tools"]["marqant"]["entrypoint"] = "src/cli.rs; locally built mq binary"
    with tempfile.TemporaryDirectory(prefix="8b-library-codecs-") as temporary:
        temporary = Path(temporary)
        for path in files:
            source = path.read_bytes()
            item = {"path": path.relative_to(ROOT).as_posix(), "bytes": len(source), "sha256": sha(source), "modes": []}
            packed = gzip.compress(source, compresslevel=9, mtime=0)
            item["modes"].append({"mode": "gzip-9", "encoded_bytes": len(packed), "operation": "roundtrip", **compare(source, gzip.decompress(packed))})
            text_input = path.suffix in (".tex", ".md", ".txt")
            if args.marqant_bin:
                modes = [("marqant-uni", "uni-encode", [], "uni-decode")]
                if text_input:
                    modes += [("marqant-default", "compress", [], "decompress"),
                              ("marqant-binary", "compress", ["--binary"], "decompress"),
                              ("marqant-semantic", "compress", ["--semantic"], "decompress"),
                              ("marqant-binary-semantic", "compress", ["--binary", "--semantic"], "decompress")]
                for mode, encoder, flags, decoder in modes:
                    encoded, decoded = temporary / "encoded", temporary / "decoded"
                    environment = {**os.environ, "MARQANT_TEST_TS": "0"}
                    run([args.marqant_bin, encoder, path, *flags, "-o", encoded], env=environment)
                    run([args.marqant_bin, decoder, encoded, "-o", decoded], env=environment)
                    item["modes"].append({"mode": mode, "encoded_bytes": encoded.stat().st_size,
                                          "operation": "roundtrip", **compare(source, decoded.read_bytes())})
            if args.bun and text_input:
                for level, name in enumerate(("verbatim", "lite", "ultra")):
                    candidate = temporary / "rewritten"
                    run([args.bun, TOOLS / "kompress-trial.ts", args.kompress_repo, path, candidate, str(level)])
                    item["modes"].append({"mode": f"kompress-{name}", "encoded_bytes": candidate.stat().st_size,
                                          "operation": "rewrite_only_no_decoder", **compare(source, candidate.read_bytes())})
            for mode in item["modes"]:
                mode["size_percent_of_original"] = round(100 * mode["encoded_bytes"] / len(source), 2)
            report["results"].append(item)
            if sha(path.read_bytes()) != item["sha256"]:
                raise RuntimeError("Source changed while measuring " + item["path"])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"Measured {len(files)} inputs. Gzip must round-trip exactly; other modes are evaluated, not presumed lossless.")
    assert all(item["modes"][0]["byte_identical"] for item in report["results"])


if __name__ == "__main__":
    main()

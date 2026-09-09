# Document compression trial

The canonical library keeps its complete [sources](../library/sources/) and
[reader editions](../library/readers/). Compression is a derived representation.
The September 9, 2026 local trial found that **gzip is the useful default for
transport; Kompress rewriting must not replace the reader or its source**.

The trial ran the actual local Marqant CLI and Kompress TypeScript rewriter on
the three revised papers, in LaTeX, PDF, and generated Markdown formats, plus a
small [fidelity fixture](fixtures/fidelity.md). Every source is identified by
SHA-256 in [results.json](results.json). Inputs were not changed. The fixture
tests literal escape tokens, decimal punctuation, equations, and qualifications.

## What was measured

| Mode | Size of the three LaTeX inputs after encoding | Exact restoration | Decision |
| --- | --- | --- | --- |
| gzip, level 9 | 39.71–42.38% of original | All inputs, including PDFs and fixture | Transport baseline |
| Marqant `compress --binary` | 53.13–56.91% | All tested text inputs | Optional codec, gated by per-file hash verification |
| Marqant default / `--semantic` | Roughly original size | Whitespace changed | Do not use as an archival replacement |
| Marqant `--binary --semantic` | 53.18–57.00% | Whitespace changed | Do not use as an archival replacement |
| Marqant `uni-encode` | 101.11–101.46% | Papers passed; fixture failed | Do not claim general losslessness |
| Kompress Verbatim | 100% | All text inputs unchanged | Pass-through |
| Kompress Lite | 93.09–95.23% | No decoder; text is rewritten | Derived context only |
| Kompress Ultra | 85.16–88.21% | No decoder; text is rewritten | Derived context only |

These are **bytes**, not LLM tokens. They do not measure search relevance,
retrieval quality, accessibility, or semantic equivalence. The results apply to
this corpus and these pinned implementations. PDF gzip sizes were 95.37–96.94%
of their originals, so the benefit there is small. No image codec was evaluated.

Marqant's CLI `--binary` mode uses token substitution, zlib, and base64 in a text
container. Its `--semantic` flag inserts section tags; it does not create a
verified research summary. Default decompression splits and rejoins lines;
semantic decompression also trims trailing whitespace. The UNI implementation
decodes literal strings such as `~H1` as reserved tokens without first escaping
them on encoding. The fixture exposes that collision even though the selected
papers happened to round-trip through UNI.

Kompress's tested `compressMessage` entrypoint uses regex rewriting. Lite
removes articles, including symbols spelled `a`; Ultra also removes words such
as `implementation`, `tests`, `and`, and `or`, and splits on periods. It is a
context reduction function with no inverse. In the Guardian LaTeX paper, our
simple diagnostic found 15 math/reference spans originally, 13 retained verbatim
after Lite, and 10 after Ultra. Counts of words such as `not` cannot certify the
meaning of the surrounding statement. Do not substitute a generated compact
representation for an equation, citation, qualification, or publication status.

## Reproduce

Python 3 runs the baseline without third-party dependencies:

```sh
python3 library-tools/compression_trial.py --output library-tools/baseline.json
```

To include both local implementations, build Marqant from its checkout. This
may download Cargo dependencies; the subsequent codec trial itself uses no
network, hosted API, credentials, or model. An external build directory keeps
build products outside the Marqant checkout. Bun runs only the pure rewriter,
without Kompress's pruning, circulation, persistence, or server entrypoints.

```sh
CARGO_TARGET_DIR=/tmp/8b-library-marqant-build \
  cargo build --locked --manifest-path ../marqant/Cargo.toml --bin mq

python3 library-tools/compression_trial.py \
  --marqant-repo ../marqant \
  --marqant-bin /tmp/8b-library-marqant-build/debug/mq \
  --kompress-repo ../forks/kompress-ultra \
  --bun "$(command -v bun)"
```

The commands assume this repository is the working directory and the sibling
repositories use those relative locations. Supply other paths when necessary.
Bun 1.4.2 was used for the recorded run. The Marqant binary was built from its
locked source checkout, rather than using an unrelated installed `mq` executable.

- Marqant: [`85c833e8e2394deae1227fa202b3289f2033a46b`](https://github.com/8b-is/marqant/tree/85c833e8e2394deae1227fa202b3289f2033a46b), package version 1.1.8; inspected [`src/cli.rs`](https://github.com/8b-is/marqant/blob/85c833e8e2394deae1227fa202b3289f2033a46b/src/cli.rs), [`src/lib.rs`](https://github.com/8b-is/marqant/blob/85c833e8e2394deae1227fa202b3289f2033a46b/src/lib.rs), and [`src/uni.rs`](https://github.com/8b-is/marqant/blob/85c833e8e2394deae1227fa202b3289f2033a46b/src/uni.rs).
- Kompress fork: commit `4cc890dbcf8cb4204495fdef1dfaaccd48bf3955`, package version 14.0.0; inspected `src/rewriter.ts` and its repository instructions. Original project: [peterlodri-sec/kompress-ultra](https://github.com/peterlodri-sec/kompress-ultra).

`results.json` records input hashes, codec revision, encoded size, output hash,
exact equality, whitespace-normalized equality, and diagnostic span/word counts.
Expected fidelity failures are findings, so the script records them rather than
treating every nonidentical rewrite as a process error. It does require the gzip
baseline to round-trip. Intermediate encodings and rewrites are temporary and
are deleted after measurement; canonical inputs remain untouched.

## Integration boundary

Reader, search, citation links, and downloads should use complete curated text.
When an optional compact context is generated, record its source revision and
hash, tool revision, mode, and whether it is lossy; link back to the original
passage. Keep it separate from the reader and require review before using it to
state a research claim. There is no production Marqant or Kompress ingestion
integration in this trial, and no blanket preservation guarantee is inferred
from passing these selected files.

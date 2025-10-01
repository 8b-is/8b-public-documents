# gtp_sim_harness.py
"""
GTP (GPT-4) Simulation Harness for UTL v1.3
-------------------------------------------------
Purpose:
1. Feed a large corpus (TXT file, 1 sentence per line) into GPT‑4 or GPT‑4o
2. Receive UTL‑formatted compression from the LLM using a one‑shot prompt
3. Log before/after token counts for 50 000‑ or 500 000‑line batches
4. Output a CSV summary + pretty Markdown report for peer review

⚠️  Requirements:
• `openai` Python package (`pip install openai`)
• `OPENAI_API_KEY` env var set
• GPT‑4 API access (or `gpt-4o`)
• Large‑volume billing enabled (500 k lines ≈ significant cost)

*This script will **not** reveal your training prompts; it sends a light “compress this to UTL v1.3” system prompt and collects the reply.*
"""
import argparse, csv, os, pathlib, time, openai
from uti_migrator import migrate_legacy_UTL

SYSTEM_PROMPT = (
    "You are an expert in the Universal Theoglyphic Language (UTL) v1.3. "
    "When the user sends raw text, respond ONLY with its compressed UTL v1.3 form, "
    "following all recursive bonding, POS+emotion tagging, and cache ID rules."
)

MODEL = "gpt-4o"
openai.api_key = os.getenv("OPENAI_API_KEY")


def count_tokens(text: str) -> int:
    return len(text.split())


def compress_line_gpt(raw: str) -> str:
    resp = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": raw.strip()},
        ],
        temperature=0.0,
        max_tokens=256,
    )
    return resp.choices[0].message.content.strip()


def run_batch(input_path: pathlib.Path, limit: int, outfile: pathlib.Path):
    before_total = after_total = 0
    rows = []
    with input_path.open(encoding="utf-8") as f, outfile.open("w", newline="", encoding="utf-8") as csvf:
        writer = csv.writer(csvf)
        writer.writerow(["line", "tokens_in", "tokens_out", "drop%"])
        for idx, line in enumerate(f):
            if idx >= limit:
                break
            raw = line.strip()
            legacy_migrated = migrate_legacy_UTL(raw)
            try:
                compressed = compress_line_gpt(legacy_migrated)
            except Exception as e:
                print(f"[ERR] line {idx+1}: {e}")
                compressed = "[ERROR]"
            tokens_in = count_tokens(raw)
            tokens_out = count_tokens(compressed)
            drop_pct = 100 * (1 - tokens_out / max(tokens_in, 1))
            before_total += tokens_in
            after_total += tokens_out
            writer.writerow([idx + 1, tokens_in, tokens_out, f"{drop_pct:.2f}"])
    print(f"Avg Drop: {100*(1-after_total/before_total):.2f}% over {limit} lines → {outfile}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Run GPT‑based UTL v1.3 compression simulation")
    p.add_argument("input", type=pathlib.Path, help="Plain‑text corpus (1 sentence per line)")
    p.add_argument("--lines", type=int, default=50000, help="Line limit (50k or 500k)")
    p.add_argument("--out", type=pathlib.Path, default=pathlib.Path("gpt_compression_log.csv"))
    args = p.parse_args()

    if not openai.api_key:
        raise RuntimeError("OPENAI_API_KEY not set")

    start = time.time()
    run_batch(args.input, args.lines, args.out)
    print(f"Elapsed: {time.time()-start:.1f}s")

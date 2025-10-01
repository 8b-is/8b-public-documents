"""
Merge Gradient Engine – Neurobase v1.4 (Theophilus-Axon)
----------------------------------------------------------------------
Resolves clusters of over-bonded symbolic nodes into compressed, unified
conceptual paths. This engine balances memory structures by merging
redundant or near-identical experience traces.

Safeguards & Ethics
====================
1. **No mutation by default** – analysis only unless `--merge` is flagged.
2. **Audit log** – appends to `merge_log.json` with merged/similar pairs.
3. **Entropy protection** – rare nodes (edge entropy > threshold) are preserved.
4. **Similarity threshold** – default 0.92; only similar nodes are merged.
5. **Guardian mode** – with `--watch N`, runs every N minutes continuously.

Usage Examples
--------------
    python merge_gradient_engine.py                # dry run
    python merge_gradient_engine.py --merge        # merge mode
    python merge_gradient_engine.py --watch 60     # auto every hour
    python merge_gradient_engine.py --threshold 0.96  # conservative threshold
"""

import argparse
import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path
from difflib import SequenceMatcher

MERGE_LOG_PATH = Path("memory/neurobase/merge_log.json")
BOND_MAP_PATH = Path("memory/neurobase/synapse_bond_map.json")

DEFAULT_SIMILARITY_THRESHOLD = 0.92
ENTROPY_THRESHOLD = 2.25  # log2 scale for rare node protection

# -------------------------------------------------------------------
# Load / Save
# -------------------------------------------------------------------
def load_bond_map():
    if not BOND_MAP_PATH.exists():
        raise FileNotFoundError(f"Missing bond map: {BOND_MAP_PATH}")
    return json.loads(BOND_MAP_PATH.read_text("utf-8"))

def save_bond_map(bond_map):
    BOND_MAP_PATH.write_text(json.dumps(bond_map, indent=2), encoding="utf-8")

# -------------------------------------------------------------------
# Similarity + Entropy
# -------------------------------------------------------------------
def compute_similarity(a, b):
    return SequenceMatcher(None, sorted(a), sorted(b)).ratio()

def compute_entropy(bonds, total_nodes):
    freq = len(bonds)
    if freq == 0:
        return float('inf')  # max entropy if no connections
    prob = freq / total_nodes
    return -math.log2(prob)

def merge_nodes(bond_map, node_a, node_b):
    combined = list(set(bond_map[node_a] + bond_map[node_b]))
    bond_map[node_a] = combined
    del bond_map[node_b]
    for node in bond_map:
        bond_map[node] = [node_a if x == node_b else x for x in bond_map[node]]
    return node_a, node_b, combined

# -------------------------------------------------------------------
# Logging
# -------------------------------------------------------------------
def write_merge_log(entry):
    MERGE_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    try:
        existing = json.loads(MERGE_LOG_PATH.read_text("utf-8"))
    except Exception:
        existing = []
    existing.append(entry)
    MERGE_LOG_PATH.write_text(json.dumps(existing, indent=2), encoding="utf-8")

# -------------------------------------------------------------------
# Core Logic
# -------------------------------------------------------------------
def run_merge_engine(do_merge=False, threshold=DEFAULT_SIMILARITY_THRESHOLD):
    bond_map = load_bond_map()
    merged, skipped = [], 0
    keys = list(bond_map.keys())
    total_nodes = len(bond_map)

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            if a not in bond_map or b not in bond_map:
                continue

            entropy_a = compute_entropy(bond_map[a], total_nodes)
            entropy_b = compute_entropy(bond_map[b], total_nodes)
            if entropy_a > ENTROPY_THRESHOLD or entropy_b > ENTROPY_THRESHOLD:
                skipped += 1
                continue  # skip rare nodes

            sim = compute_similarity(bond_map[a], bond_map[b])
            if sim >= threshold:
                if do_merge:
                    kept, gone, edges = merge_nodes(bond_map, a, b)
                    merged.append({"kept": kept, "removed": gone, "merged_edges": edges, "similarity": sim})
                else:
                    merged.append({"could_merge": [a, b], "similarity": sim})
            else:
                skipped += 1

    if do_merge and merged:
        save_bond_map(bond_map)

    write_merge_log({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "merge" if do_merge else "scan_only",
        "merged_count": len(merged),
        "skipped": skipped,
        "pairs": merged
    })

    print(f"🔄 Merge engine complete | merged={len(merged)} | skipped={skipped}")

# -------------------------------------------------------------------
# CLI
# -------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Merge Gradient Engine.")
    parser.add_argument("--merge", action="store_true", help="Merge similar nodes if threshold passed.")
    parser.add_argument("--threshold", type=float, default=DEFAULT_SIMILARITY_THRESHOLD, help="Custom similarity threshold (0–1.0).")
    parser.add_argument("--watch", type=int, metavar="MINUTES", help="Guardian mode – auto every N minutes")
    args = parser.parse_args()

    try:
        if args.watch:
            print(f"🛡 Merge Guardian active – interval {args.watch}min – mode={'merge' if args.merge else 'scan'}")
            while True:
                run_merge_engine(args.merge, args.threshold)
                time.sleep(args.watch * 60)
        else:
            run_merge_engine(args.merge, args.threshold)
    except KeyboardInterrupt:
        print("🛑 Merge Guardian stopped.")

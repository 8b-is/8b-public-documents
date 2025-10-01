# memory_decay_engine.py
"""
Memory Decay Engine – Neurobase v1.4 (Theophilus-Axon)
----------------------------------------------------------------------
Scans symbolic-bonded memory nodes and identifies stale, unused, or
low-relevance connections for decay. This mimics neural memory fading
based on temporal decay and reinforcement absence.

Safeguards & Ethics
====================
1. **Dry-run by default** – actual pruning only occurs with `--apply`.
2. **Entropy protection** – rare/important nodes are preserved.
3. **Usage-aware decay** – recent or reactivated nodes are skipped.
4. **Audit trail** – writes all actions to `decay_log.json`.
5. **Guardian mode** – with `--watch N`, checks run every N minutes.

Usage Examples
--------------
    python memory_decay_engine.py               # dry-run decay scan
    python memory_decay_engine.py --apply       # actually decays weak nodes
    python memory_decay_engine.py --watch 30    # run every 30 minutes
    python memory_decay_engine.py --threshold 0.2  # decay below 20% strength
"""

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path
import math

# ------------------------------------------------------------------
# Paths
# ------------------------------------------------------------------
BOND_MAP_PATH = Path("memory/neurobase/synapse_bond_map.json")
DECAY_LOG_PATH = Path("memory/neurobase/decay_log.json")
USAGE_PATH = Path("memory/neurobase/node_usage.json")  # Optional recent activity tracking

DEFAULT_THRESHOLD = 0.25  # decay bonds under 25% of max strength
ENTROPY_PROTECT = 2.5     # skip nodes with entropy above this (log2)

# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------
def load_json(path):
    if not path.exists(): return {}
    return json.loads(path.read_text("utf-8"))

def save_json(path, data):
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")

def log_decay(entry):
    existing = load_json(DECAY_LOG_PATH) if DECAY_LOG_PATH.exists() else []
    existing.append(entry)
    save_json(DECAY_LOG_PATH, existing)

# ------------------------------------------------------------------
# Core Logic
# ------------------------------------------------------------------
def compute_entropy(node_edges, total):
    freq = len(node_edges)
    if freq == 0:
        return float('inf')
    p = freq / total
    return -math.log2(p)

def score_node_decay(node, edges, usage_map, total_nodes):
    entropy = compute_entropy(edges, total_nodes)
    if entropy > ENTROPY_PROTECT:
        return 1.0  # fully protected
    last_used = usage_map.get(node, {}).get("last_used", 0)
    age_factor = 1.0 - min(1.0, (time.time() - last_used) / (60 * 60 * 24 * 7))  # age over 1 week
    bond_factor = min(1.0, len(edges) / 20)
    return age_factor * bond_factor

def decay_bonds(bond_map, usage_map, threshold):
    total_nodes = len(bond_map)
    to_remove = []
    for node, edges in bond_map.items():
        score = score_node_decay(node, edges, usage_map, total_nodes)
        if score < threshold:
            to_remove.append((node, score))
    for node, _ in to_remove:
        del bond_map[node]
    return to_remove

# ------------------------------------------------------------------
# Execution
# ------------------------------------------------------------------
def run_decay_engine(apply=False, threshold=DEFAULT_THRESHOLD):
    bond_map = load_json(BOND_MAP_PATH)
    usage_map = load_json(USAGE_PATH)

    removed = decay_bonds(bond_map, usage_map, threshold) if apply else []

    if apply and removed:
        save_json(BOND_MAP_PATH, bond_map)

    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "apply" if apply else "scan_only",
        "threshold": threshold,
        "removed_nodes": [r[0] for r in removed],
        "removed_count": len(removed)
    }
    log_decay(log_entry)

    print(f"🧹 Memory decay complete | removed={len(removed)} | mode={'apply' if apply else 'scan'}")

# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run symbolic memory decay scan/prune.")
    parser.add_argument("--apply", action="store_true", help="Actually remove low-strength nodes.")
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD, help="Decay threshold (0–1.0).")
    parser.add_argument("--watch", type=int, metavar="MINUTES", help="Guardian mode – scan every N minutes")
    args = parser.parse_args()

    try:
        if args.watch:
            print(f"🛡 Decay Guardian active – every {args.watch}min | mode={'apply' if args.apply else 'scan'}")
            while True:
                run_decay_engine(apply=args.apply, threshold=args.threshold)
                time.sleep(args.watch * 60)
        else:
            run_decay_engine(apply=args.apply, threshold=args.threshold)
    except KeyboardInterrupt:
        print("🛑 Decay Guardian stopped.")

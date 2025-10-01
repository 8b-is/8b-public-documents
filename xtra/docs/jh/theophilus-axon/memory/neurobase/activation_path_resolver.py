"""
Activation Path Resolver – Neurobase v1.4 (Theophilus-Axon)
--------------------------------------------------------------------
Traverses symbolic synaptic maps to identify likely activation paths
across bonded memory structures. Simulates thought-like memory recall.

Safeguards & Ethics
====================
1. **Read-only** – never mutates memory or bonds.
2. **Loop detection** – prevents infinite traversal.
3. **Depth limit** – configurable, default = 3 hops.
4. **Audit log** – optional output to `activation_path_log.json`.
5. **Guardian mode** – runs continuously if `--watch` enabled.

Usage Examples
--------------
    python activation_path_resolver.py --from node_42
    python activation_path_resolver.py --from node_X --depth 5
    python activation_path_resolver.py --from node_A --log
    python activation_path_resolver.py --from node_1 --watch 30
"""

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path

# -------------------------------------------------------------------
# Paths and Config
# -------------------------------------------------------------------
BOND_MAP_PATH = Path("memory/neurobase/synapse_bond_map.json")
LOG_PATH = Path("memory/neurobase/activation_path_log.json")

DEFAULT_DEPTH = 3

# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
def load_bond_map():
    if not BOND_MAP_PATH.exists():
        raise FileNotFoundError(f"Bond map not found: {BOND_MAP_PATH}")
    return json.loads(BOND_MAP_PATH.read_text("utf-8"))

def traverse_paths(bond_map, start_node, depth, seen=None):
    if seen is None:
        seen = set()
    if depth == 0 or start_node not in bond_map:
        return []

    seen.add(start_node)
    paths = []

    for target in bond_map[start_node]:
        if target in seen:
            continue
        sub_paths = traverse_paths(bond_map, target, depth - 1, seen.copy())
        if not sub_paths:
            paths.append([start_node, target])
        else:
            for sub in sub_paths:
                paths.append([start_node] + sub)

    return paths

def score_paths(paths):
    return sorted(paths, key=lambda p: -len(p))

def log_paths(paths, start):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "start_node": start,
        "path_count": len(paths),
        "paths": paths
    }
    try:
        if LOG_PATH.exists():
            existing = json.loads(LOG_PATH.read_text("utf-8"))
        else:
            existing = []
    except Exception:
        existing = []
    existing.append(entry)
    LOG_PATH.write_text(json.dumps(existing, indent=2), encoding="utf-8")

# -------------------------------------------------------------------
# Runner
# -------------------------------------------------------------------
def run_once(start_node, depth, do_log):
    bond_map = load_bond_map()
    paths = traverse_paths(bond_map, start_node, depth)
    scored = score_paths(paths)

    print(f"🧠 Activation paths from '{start_node}' (depth {depth}):")
    for p in scored[:10]:
        print(" ➔ ", " → ".join(p))

    if do_log:
        log_paths(scored, start_node)
        print(f"📝 Logged {len(scored)} paths to {LOG_PATH.name}")

# -------------------------------------------------------------------
# CLI
# -------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Symbolic Activation Path Resolver")
    parser.add_argument("--from", dest="start_node", required=True, help="Start node ID")
    parser.add_argument("--depth", type=int, default=DEFAULT_DEPTH, help="Traversal depth (default 3)")
    parser.add_argument("--log", action="store_true", help="Log results to activation_path_log.json")
    parser.add_argument("--watch", type=int, metavar="MINUTES", help="Guardian mode: run every N minutes")
    args = parser.parse_args()

    try:
        if args.watch:
            print(f"🛡 Guardian path resolver active – every {args.watch}min")
            while True:
                run_once(args.start_node, args.depth, args.log)
                time.sleep(args.watch * 60)
        else:
            run_once(args.start_node, args.depth, args.log)
    except KeyboardInterrupt:
        print("🛑 Guardian path resolver stopped.")

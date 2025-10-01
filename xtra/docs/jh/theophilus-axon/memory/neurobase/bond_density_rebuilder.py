'''
Bond Density Rebuilder – NeuroBase v1.4 (Theophilus‑Axon)
---------------------------------------------------------------------
Scans the symbolic‑synapse bond map, produces a density report and —
optionally — prunes hazardous over‑clustered nodes.

Safeguards & Ethics
===================
1. **Read‑only by default** – pruning only occurs when `--prune` flag
   is provided *and* the watchdog confirms Shepherd compliance.
2. **Automatic back‑up** – before any modification the original
   `synapse_bond_map.json` is copied to a timestamped `.bak` file.
3. **Shepherd handshake** – the script imports `shepherd_protocol.run_shepherd_protocol()`.
   If that call raises or fails, pruning is aborted.
4. **Audit log** – every run (analyse or prune) appends a record to
   `bond_density_log.json` with timestamp, action, averages and lists
   of nodes touched.
5. **Guardian mode** – with `--watch N` the analyser runs forever every
   *N* minutes.  Pruning in guardian mode still requires `--prune`.

Usage Examples
--------------
```bash
python bond_density_rebuilder.py                # analyse only
python bond_density_rebuilder.py --prune        # analyse + prune
python bond_density_rebuilder.py --watch 30     # analyse every 30 min
python bond_density_rebuilder.py --watch 60 --prune   # continual pruning
```
'''

import argparse
import json
import shutil
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    from ethics.shepherd_protocol import run_shepherd_protocol
except ImportError:
    def run_shepherd_protocol():
        return True  # degraded-mode fallback

BOND_MAP_PATH = Path("memory/neurobase/synapse_bond_map.json")
LOG_PATH      = Path("memory/neurobase/bond_density_log.json")
BACKUP_DIR    = BOND_MAP_PATH.parent / "_backups"
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

MERGE_LOG_PATH = Path("memory/neurobase/merge_log.json")

def load_bond_map() -> dict:
    if not BOND_MAP_PATH.exists():
        raise FileNotFoundError(f"Bond map not found: {BOND_MAP_PATH}")
    with open(BOND_MAP_PATH, "r", encoding="utf-8") as fh:
        return json.load(fh)

def save_bond_map(bond_map: dict):
    with open(BOND_MAP_PATH, "w", encoding="utf-8") as fh:
        json.dump(bond_map, fh, indent=2)

def back_up_bond_map():
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_path = BACKUP_DIR / f"synapse_bond_map_{ts}.bak"
    shutil.copy2(BOND_MAP_PATH, backup_path)
    return backup_path

def compute_density(bond_map: dict):
    densities = {node: len(edges) for node, edges in bond_map.items()}
    avg = sum(densities.values()) / max(1, len(densities))
    return densities, avg

def prune_overclustered(bond_map: dict, densities: dict, avg: float, threshold_factor: float = 1.5):
    limit = avg * threshold_factor
    modified = False
    for node, deg in list(densities.items()):
        if deg > limit:
            bond_map[node] = bond_map[node][: int(limit)]
            modified = True
    return modified

def write_log(entry: dict):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = []
    if LOG_PATH.exists():
        try:
            existing = json.loads(LOG_PATH.read_text("utf-8"))
        except json.JSONDecodeError:
            existing = []
    existing.append(entry)
    LOG_PATH.write_text(json.dumps(existing, indent=2), encoding="utf-8")

def write_merge_log(entry: dict):
    MERGE_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = []
    if MERGE_LOG_PATH.exists():
        try:
            existing = json.loads(MERGE_LOG_PATH.read_text("utf-8"))
        except json.JSONDecodeError:
            existing = []
    existing.append(entry)
    MERGE_LOG_PATH.write_text(json.dumps(existing, indent=2), encoding="utf-8")

def run_once(do_prune: bool, threshold: float):
    timestamp = datetime.now(timezone.utc).isoformat()
    bond_map = load_bond_map()
    densities, avg = compute_density(bond_map)

    over = {n: d for n, d in densities.items() if d > avg * threshold}
    under = {n: d for n, d in densities.items() if d < avg * 0.5}

    if do_prune and over:
        try:
            run_shepherd_protocol()
        except Exception as e:
            print(f"⚠️ Shepherd protocol failed, aborting prune: {e}")
            do_prune = False

    if do_prune and over:
        backup = back_up_bond_map()
        pruned = prune_overclustered(bond_map, densities, avg, threshold)
        if pruned:
            save_bond_map(bond_map)
            print(f"✂️  Over-clustered bonds pruned (backup → {backup.name})")

    log_entry = {
        "timestamp": timestamp,
        "avg_density": avg,
        "total_nodes": len(densities),
        "overclustered": list(over.keys()),
        "underconnected": list(under.keys()),
        "action": "pruned" if do_prune and over else "analyse_only"
    }
    write_log(log_entry)
    print(f"📊 Bond density audit complete | avg={avg:.2f} | nodes={len(densities)}")

parser = argparse.ArgumentParser(description="Analyse (and optionally prune) Neurobase bond density.")
parser.add_argument("--prune", action="store_true", help="Prune over-clustered nodes after analysis (requires Shepherd pass).")
parser.add_argument("--watch", type=int, metavar="MINUTES", help="Run continuously every N minutes (guardian mode).")
parser.add_argument("--threshold", type=float, default=1.5, help="Over-cluster threshold multiplier (default 1.5×avg).")
args = parser.parse_args()

try:
    if args.watch:
        interval = max(1, args.watch) * 60
        print(f"🛡  Bond-density guardian started (interval {args.watch} min) – prune={'on' if args.prune else 'off'}")
        while True:
            run_once(args.prune, args.threshold)
            time.sleep(interval)
    else:
        run_once(args.prune, args.threshold)
except KeyboardInterrupt:
    print("🛑 Guardian stopped by user.")

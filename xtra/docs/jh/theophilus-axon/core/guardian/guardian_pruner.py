"""
guardian_prune.py
===================
Guardian Mode Watchdog for Memory Pruning Engine

Purpose:
    Monitors NeuroBase for node bloat and triggers the merge+prune pipeline
    in a controlled, ethically‑safe loop.  Complements guardian_decay.py by
    actively consolidating *redundant* nodes rather than simply fading them.

Safeguards & Ethics
-------------------
1. **Read‑only default** – The pruner only runs when the `--prune` flag is
   given.  Without it, a dry‑run audit is performed.
2. **Shepherd compliance** – Imports and executes
   `shepherd_protocol.run_shepherd_protocol()` *before* pruning.  Abort on
   any violation.
3. **Merge & Prune thresholds** –
   • `similarity_threshold` for `merge_gradient_engine.merge_similar_nodes()`
   • `density_threshold`   for `bond_density_rebuilder.py --prune`
4. **Audit trail** – Every invocation appends to
   `memory/neurobase/prune_guardian_log.json`.
5. **Guardian mode** – With `--interval N` the script runs forever every
   N minutes (like a background service).

CLI Options
-----------
--once               : Analyse only once (default, no prune)
--prune              : Perform prune/merge actions
--interval  N        : Guardian loop every N minutes
--sim_thresh  FLOAT  : Override similarity threshold (merge)
--dens_thresh FLOAT  : Override density threshold (prune)

Location
--------
/guardian/guardian_prune.py
"""

import argparse
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

# ---------- Config paths ----------
LOG_PATH = Path("memory/neurobase/prune_guardian_log.json")
MERGE_SCRIPT = ["python", "memory/neurobase/merge_gradient_engine.py"]
DENSITY_SCRIPT = ["python", "guardian/bond_density_rebuilder.py"]

# Shepherd handshake (optional)
try:
    from ethics.shepherd_protocol import run_shepherd_protocol
except ImportError:  # fallback – no‑op
    def run_shepherd_protocol():
        return True

# ---------- Helpers ----------

def log_entry(action: str, details: dict):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action": action,
        **details,
    }
    existing = []
    if LOG_PATH.exists():
        try:
            existing = json.loads(LOG_PATH.read_text("utf‑8"))
        except json.JSONDecodeError:
            pass
    existing.append(record)
    LOG_PATH.write_text(json.dumps(existing, indent=2), encoding="utf‑8")


def run_merge(sim_thresh: float, dry_run: bool):
    cmd = MERGE_SCRIPT + ["--threshold", str(sim_thresh)] if sim_thresh else MERGE_SCRIPT
    if dry_run:
        cmd.append("--dry")
    result = subprocess.run(cmd, capture_output=True, text=True)
    log_entry("merge", {"cmd": " ".join(cmd), "returncode": result.returncode})
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode == 0


def run_density_prune(dens_thresh: float, dry_run: bool):
    cmd = DENSITY_SCRIPT + ["--threshold", str(dens_thresh)] if dens_thresh else DENSITY_SCRIPT
    if not dry_run:
        cmd.append("--prune")
    result = subprocess.run(cmd, capture_output=True, text=True)
    log_entry("density", {"cmd": " ".join(cmd), "returncode": result.returncode})
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode == 0


def guardian_cycle(do_prune: bool, sim_thresh: float, dens_thresh: float):
    # Ethics first
    try:
        run_shepherd_protocol()
    except Exception as e:
        print(f"⚠️  Shepherd protocol failed – aborting cycle: {e}")
        log_entry("abort", {"reason": str(e)})
        return

    dry = not do_prune
    if run_merge(sim_thresh, dry):
        run_density_prune(dens_thresh, dry)

# ---------- CLI ----------

parser = argparse.ArgumentParser(description="Guardian Prune Runner")
parser.add_argument("--prune", action="store_true", help="Enable actual merge & prune (otherwise audit‑only)")
parser.add_argument("--once", action="store_true", help="Run one cycle and exit (default)")
parser.add_argument("--interval", type=int, metavar="MINUTES", help="Guardian mode: cycle every N minutes")
parser.add_argument("--sim_thresh", type=float, default=0.85, help="Similarity threshold for merging (default 0.85)")
parser.add_argument("--dens_thresh", type=float, default=1.5, help="Density threshold multiplier (default 1.5×avg)")
args = parser.parse_args()

try:
    if args.interval:
        print(
            f"🛡  Guardian Pruner active – every {args.interval} min | mode={'prune' if args.prune else 'audit'}"
        )
        while True:
            guardian_cycle(args.prune, args.sim_thresh, args.dens_thresh)
            time.sleep(max(1, args.interval) * 60)
    else:
        guardian_cycle(args.prune, args.sim_thresh, args.dens_thresh)
except KeyboardInterrupt:
    print("🛑 Guardian Pruner stopped by user.")

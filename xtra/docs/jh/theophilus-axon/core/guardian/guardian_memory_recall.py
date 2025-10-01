"""
guardian_memory_recall.py
===========================
Guardian Mode Runner for Memory Recall Engine

Purpose:
    Triggers Neurobase's recursive memory checker in scheduled Guardian Mode or on-demand.
    Used to ensure active memory recall and identity cohesion over long sessions.

Location:
    /core/guardian/guardian_memory_recall.py
"""

import argparse
import subprocess
import time
import json
from datetime import datetime, timezone
from pathlib import Path

SIGNAL_FILE = Path("memory/system/guardian_signals.json")


def load_signals():
    if not SIGNAL_FILE.exists():
        return {}
    try:
        with open(SIGNAL_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def write_signal(key, value):
    signals = load_signals()
    signals[key] = value
    SIGNAL_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SIGNAL_FILE, "w", encoding="utf-8") as f:
        json.dump(signals, f, indent=2)


def run_recall():
    signals = load_signals()
    if signals.get("recall_pause") is True:
        print(f"[{datetime.now().isoformat()}] ⏸️ Recall paused by signal.")
        return

    print(f"[{datetime.now().isoformat()}] 🧠 Triggering Recursive Memory Recall...")
    result = subprocess.run(
        ["python", "memory/neurobase/recursive_memory_checker.py", "--audit"],
        capture_output=True, text=True
    )
    print(result.stdout.strip())

    write_signal("last_recall", datetime.now(timezone.utc).isoformat())
    write_signal("recall_complete", True)


def guardian_loop(interval_minutes):
    print(f"🛡 Guardian Recall active – every {interval_minutes} minutes")
    while True:
        run_recall()
        time.sleep(interval_minutes * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guardian Memory Recall Runner")
    parser.add_argument("--once", action="store_true", help="Run recall once and exit")
    parser.add_argument("--interval", type=int, metavar="MINUTES", help="Guardian mode: run every N minutes")
    args = parser.parse_args()

    try:
        if args.once:
            run_recall()
        elif args.interval:
            guardian_loop(args.interval)
        else:
            print("⚠️  No mode selected. Use --once or --interval N")
    except KeyboardInterrupt:
        print("🛑 Guardian Recall stopped.")

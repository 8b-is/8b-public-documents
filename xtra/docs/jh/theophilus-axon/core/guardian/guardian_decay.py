"""
guardian_decay.py
===================
Guardian Mode Watchdog for Memory Decay Engine

Purpose:
    Runs the Neurobase memory_decay_engine.py in safe recurring intervals
    to simulate forgetting and keep symbolic weight balanced over time.

Modes:
    --once            : Run decay once (useful for batch jobs)
    --interval N      : Run decay every N minutes (Guardian Mode)

Location:
    /guardian/guardian_decay.py
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

def run_decay():
    signals = load_signals()
    if signals.get("decay_pause") is True:
        print(f"[{datetime.now().isoformat()}] ⏸️ Decay paused by signal.")
        return

    print(f"[{datetime.now().isoformat()}] 🧠 Triggering Memory Decay...")
    result = subprocess.run(["python", "memory/neurobase/memory_decay_engine.py", "--apply"], capture_output=True, text=True)
    print(result.stdout.strip())

    write_signal("last_decay", datetime.now(timezone.utc).isoformat())
    write_signal("decay_complete", True)

def guardian_loop(interval_minutes):
    print(f"🛡 Guardian Decay active – every {interval_minutes} minutes")
    while True:
        run_decay()
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guardian Decay Runner")
    parser.add_argument("--once", action="store_true", help="Run decay once and exit")
    parser.add_argument("--interval", type=int, metavar="MINUTES", help="Guardian mode: run every N minutes")
    args = parser.parse_args()

    try:
        if args.once:
            run_decay()
        elif args.interval:
            guardian_loop(args.interval)
        else:
            print("⚠️  No mode selected. Use --once or --interval N")
    except KeyboardInterrupt:
        print("🛑 Guardian Decay stopped.")

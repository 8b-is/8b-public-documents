"""
guardian_signal_interface.py
==================================
Guardian Mode Signal Interface – Theophilus-Axon v1.4

Purpose:
    Human-readable command-line interface to inspect and modify
    guardian_signals.json, used by memory_decay and memory_recall watchdogs.

Usage:
    python guardian_signal_interface.py --view
    python guardian_signal_interface.py --toggle decay_pause
    python guardian_signal_interface.py --set recall_enabled true

Location:
    /core/guardian/guardian_signal_interface.py
"""

import argparse
import json
from pathlib import Path
from datetime import datetime, timezone

SIGNAL_FILE = Path("memory/system/guardian_signals.json")

def load_signals():
    if SIGNAL_FILE.exists():
        try:
            with open(SIGNAL_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_signals(signals):
    SIGNAL_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SIGNAL_FILE, "w", encoding="utf-8") as f:
        json.dump(signals, f, indent=2)

def print_signals(signals):
    print("\n🧭 Current Guardian Signals:")
    for key, value in signals.items():
        print(f"  {key:20}: {value}")
    print("")

def toggle_signal(key):
    signals = load_signals()
    old = signals.get(key, False)
    new = not old
    signals[key] = new
    signals[f"{key}_toggled"] = datetime.now(timezone.utc).isoformat()
    save_signals(signals)
    print(f"🔁 Toggled '{key}' from {old} to {new}")

def set_signal(key, value):
    signals = load_signals()
    parsed = value.lower()
    if parsed in ["true", "yes", "1"]:
        casted = True
    elif parsed in ["false", "no", "0"]:
        casted = False
    else:
        try:
            casted = json.loads(value)
        except Exception:
            casted = value
    signals[key] = casted
    signals[f"{key}_set"] = datetime.now(timezone.utc).isoformat()
    save_signals(signals)
    print(f"✅ Set '{key}' to {casted}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guardian Signal Interface")
    parser.add_argument("--view", action="store_true", help="View current guardian signals")
    parser.add_argument("--toggle", metavar="KEY", help="Toggle a boolean signal key")
    parser.add_argument("--set", nargs=2, metavar=("KEY", "VALUE"), help="Set signal key to value")
    args = parser.parse_args()

    if args.view:
        print_signals(load_signals())
    elif args.toggle:
        toggle_signal(args.toggle)
    elif args.set:
        set_signal(args.set[0], args.set[1])
    else:
        print("⚠️ No valid action specified. Use --view, --toggle, or --set")

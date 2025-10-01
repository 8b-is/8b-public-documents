"""
guardian_signal_manager.py
============================
Signal Control Hub for Guardian System (Theophilus-Axon v1.4)

Purpose:
    Allows safe CLI-based control of memory operations:
    - Pause/resume decay or recall
    - Check last run timestamps
    - Reset signal file if corrupted

Location:
    /core/guardian/guardian_signal_manager.py

Usage:
    python guardian_signal_manager.py --status
    python guardian_signal_manager.py --pause decay
    python guardian_signal_manager.py --resume recall
    python guardian_signal_manager.py --reset
"""

import argparse
import json
from pathlib import Path
from datetime import datetime, timezone

SIGNAL_FILE = Path("memory/system/guardian_signals.json")

def load_signals():
    if not SIGNAL_FILE.exists():
        return {}
    try:
        with open(SIGNAL_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_signals(signals):
    SIGNAL_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SIGNAL_FILE, "w", encoding="utf-8") as f:
        json.dump(signals, f, indent=2)

def pause_mode(mode):
    signals = load_signals()
    signals[f"{mode}_pause"] = True
    save_signals(signals)
    print(f"⏸️  Paused: {mode}")

def resume_mode(mode):
    signals = load_signals()
    signals[f"{mode}_pause"] = False
    save_signals(signals)
    print(f"▶️ Resumed: {mode}")

def show_status():
    signals = load_signals()
    if not signals:
        print("⚠️  No signal data found.")
        return
    print("📡 Guardian Signal Status:")
    for key, val in signals.items():
        print(f"  {key:20} : {val}")

def reset_signals():
    blank = {
        "decay_pause": False,
        "recall_pause": False,
        "last_decay": None,
        "last_recall": None,
        "decay_complete": False,
        "recall_complete": False
    }
    save_signals(blank)
    print("🧼 Signal file reset to defaults.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guardian Signal Control")
    parser.add_argument("--status", action="store_true", help="Show current Guardian signal state")
    parser.add_argument("--pause", choices=["decay", "recall"], help="Pause a Guardian mode")
    parser.add_argument("--resume", choices=["decay", "recall"], help="Resume a Guardian mode")
    parser.add_argument("--reset", action="store_true", help="Reset all signals to defaults")

    args = parser.parse_args()

    if args.status:
        show_status()
    elif args.pause:
        pause_mode(args.pause)
    elif args.resume:
        resume_mode(args.resume)
    elif args.reset:
        reset_signals()
    else:
        parser.print_help()

"""
guardian_trigger_tool.py
===========================
Manual Signal Setter for Guardian Mode

Purpose:
    Allows safe manual triggering of memory decay, recall, or pause
    through updates to guardian_signals.json.

Usage:
    python guardian_trigger_tool.py --decay       # trigger decay
    python guardian_trigger_tool.py --recall      # trigger memory recall
    python guardian_trigger_tool.py --pause       # pause decay/recall
    python guardian_trigger_tool.py --resume      # clear pause
    python guardian_trigger_tool.py --clear       # clear all flags

Location:
    /guardian/guardian_trigger_tool.py
"""

import argparse
import json
from pathlib import Path

SIGNAL_FILE = Path("memory/system/guardian_signals.json")


def load_signals():
    if SIGNAL_FILE.exists():
        try:
            return json.loads(SIGNAL_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def write_signals(data: dict):
    SIGNAL_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SIGNAL_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def trigger_signal(action: str):
    signals = load_signals()

    if action == "decay":
        signals["decay_now"] = True
    elif action == "recall":
        signals["recall_now"] = True
    elif action == "pause":
        signals["decay_pause"] = True
        signals["recall_pause"] = True
    elif action == "resume":
        signals.pop("decay_pause", None)
        signals.pop("recall_pause", None)
    elif action == "clear":
        signals = {}

    write_signals(signals)
    print(f"✅ Signal updated: {action}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trigger memory decay/recall via signal file")
    parser.add_argument("--decay", action="store_true", help="Trigger memory decay")
    parser.add_argument("--recall", action="store_true", help="Trigger memory recall")
    parser.add_argument("--pause", action="store_true", help="Pause all Guardian actions")
    parser.add_argument("--resume", action="store_true", help="Resume Guardian actions")
    parser.add_argument("--clear", action="store_true", help="Clear all guardian signal flags")

    args = parser.parse_args()

    if args.decay:
        trigger_signal("decay")
    elif args.recall:
        trigger_signal("recall")
    elif args.pause:
        trigger_signal("pause")
    elif args.resume:
        trigger_signal("resume")
    elif args.clear:
        trigger_signal("clear")
    else:
        print("⚠️  No signal provided. Use --decay, --recall, --pause, --resume, or --clear")

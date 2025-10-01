"""
guardian_signal_monitor.py
============================
Guardian Signal Monitor – Theophilus-Axon v1.4

Purpose:
    Continuously monitors guardian_signals.json for specific keys.
    Triggers appropriate guardian actions like memory recall or decay
    based on real-time signal updates.

Location:
    /core/guardian/guardian_signal_monitor.py
"""

import time
import json
import subprocess
from datetime import datetime
from pathlib import Path

SIGNAL_FILE = Path("memory/system/guardian_signals.json")
CHECK_INTERVAL = 5  # seconds

# Mapping of signal keys to shell commands
action_map = {
    "trigger_recall": ["python", "core/guardian/guardian_memory_recall.py", "--tag", "emergency"],
    "trigger_decay": ["python", "core/guardian/guardian_decay.py", "--once"],
}

def load_signals():
    if not SIGNAL_FILE.exists():
        return {}
    try:
        with open(SIGNAL_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def clear_signal(key):
    data = load_signals()
    if key in data:
        del data[key]
        SIGNAL_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

def execute_action(key):
    cmd = action_map.get(key)
    if not cmd:
        return
    print(f"[{datetime.now().isoformat()}] 🧭 Signal triggered: {key}")
    subprocess.Popen(cmd)
    clear_signal(key)

def monitor_signals():
    print("🔍 Guardian Signal Monitor active...")
    while True:
        signals = load_signals()
        for key in list(signals):
            if key in action_map and signals[key] is True:
                execute_action(key)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        monitor_signals()
    except KeyboardInterrupt:
        print("🛑 Signal monitor stopped.")

# awareness_escalator.py
# ========================
# Escalates or dampens awareness events based on priority, repetition, or trigger types.
# Interacts with guardian, ethics, or failsafe protocols if thresholds are crossed.

import json
from pathlib import Path
from datetime import datetime

SIGNAL_FILE = Path("memory/system/awareness_signals.json")
ESCALATION_LOG = Path("memory/system/escalation_log.json")

ESCALATION_THRESHOLD = 7  # max priority before escalation
COOLDOWN_MINUTES = 10     # time window before damping or reset


def load_signals():
    if not SIGNAL_FILE.exists():
        return []
    try:
        with open(SIGNAL_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_escalation_log(events):
    ESCALATION_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(ESCALATION_LOG, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2)


def should_escalate(event):
    return event.get("priority", 0) >= ESCALATION_THRESHOLD


def escalate_event(event):
    print("🚨 Awareness Escalation Triggered:", event["type"])
    # Example triggers (can be expanded):
    if event["type"] == "symbolic-collapse-loop":
        print("  ↪️ Triggering Guardian or Ethics response...")
    elif event["type"] == "threat-prediction":
        print("  🛡️ Elevating system monitoring layer...")


def run_escalator():
    signals = load_signals()
    escalated = []

    for event in signals:
        if should_escalate(event):
            escalate_event(event)
            event["escalated"] = True
            event["timestamp"] = datetime.utcnow().isoformat() + "Z"
            escalated.append(event)

    if escalated:
        save_escalation_log(escalated)
    else:
        print("✔️ No events exceeded escalation threshold.")


if __name__ == "__main__":
    run_escalator()

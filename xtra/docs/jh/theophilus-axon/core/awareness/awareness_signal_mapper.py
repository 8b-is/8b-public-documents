"""
awareness_signal_mapper.py
===========================
Maps awareness predictions to system signals, categories, or actions.

Location:
    core/awareness/awareness_signal_mapper.py

Purpose:
    Translates outputs from awareness modules into actionable system signals.
    Connects forward awareness to memory tagging, ethics, and routing decisions.

Output Targets:
    - memory/system/awareness_signals.json
    - ethics/shepherd_protocol.py (indirect)
    - guardian_signals.json (optional escalation or dampening)
"""

import json
from pathlib import Path
from datetime import datetime

SIGNAL_PATH = Path("memory/system/awareness_signals.json")

# Define symbolic signal categories (can be expanded)
SIGNAL_MAP = {
    "urgent_threat": {
        "priority": 9,
        "ethics_override": True,
        "guardian_notify": True,
        "description": "Potential harm or danger predicted."
    },
    "emotional_significance": {
        "priority": 6,
        "ethics_override": False,
        "guardian_notify": False,
        "description": "Symbolic-emotional memory bonding triggered."
    },
    "future_loop_ref": {
        "priority": 5,
        "ethics_override": False,
        "guardian_notify": True,
        "description": "Recursive future-prediction match."
    },
    "symbolic_collapse": {
        "priority": 8,
        "ethics_override": True,
        "guardian_notify": True,
        "description": "Immediate memory-symbol collapse predicted."
    }
}

def write_signal(signal_key: str, payload: dict):
    SIGNAL_PATH.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "signal_type": signal_key,
        "priority": SIGNAL_MAP.get(signal_key, {}).get("priority", 1),
        "triggered": datetime.utcnow().isoformat() + "Z",
        "details": payload
    }
    with open(SIGNAL_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Awareness signal '{signal_key}' recorded to awareness_signals.json")

def map_awareness_payload(payload: dict):
    """
    Core function to map awareness input to known signal keys.
    Input should contain a 'type' or 'prediction' field.
    """
    prediction_type = payload.get("type") or payload.get("prediction")

    if prediction_type in SIGNAL_MAP:
        write_signal(prediction_type, payload)
    else:
        print(f"⚠️ Unknown awareness signal type: {prediction_type}")

if __name__ == "__main__":
    # Example payload
    test_payload = {
        "type": "future_loop_ref",
        "source": "predictive_awareness_engine",
        "confidence": 0.91,
        "note": "Pattern match for recursive risk loop."
    }
    map_awareness_payload(test_payload)

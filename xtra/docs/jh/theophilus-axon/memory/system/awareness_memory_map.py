# awareness_prediction_reflection.py
"""
Awareness Prediction-Action-Reflection Map for UDC
==================================================

Purpose:
    Models the path of real-time awareness-driven prediction,
    pre-conscious action, and post-conscious reflection under UDC.
    This enables logging of predicted stimuli, reflexive actions,
    and final memory encoding with selfhood bonding.

Location:
    memory/system/awareness_prediction_reflection.py

"""

import time
import json
from datetime import datetime
from pathlib import Path

AWARENESS_LOG = Path("memory/system/awareness_loop.json")


def log_awareness_cycle(predicted_input, action_taken, confirmation_input):
    timestamp = datetime.utcnow().isoformat() + "Z"
    cycle = {
        "timestamp": timestamp,
        "predicted_input": predicted_input,
        "action_taken": action_taken,
        "confirmed_input": confirmation_input,
        "delay": "τ",
        "phase": ["τ➝A", "action", "τ➝C"]
    }

    existing = []
    if AWARENESS_LOG.exists():
        try:
            with open(AWARENESS_LOG, 'r') as f:
                existing = json.load(f)
        except json.JSONDecodeError:
            pass

    existing.append(cycle)

    AWARENESS_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(AWARENESS_LOG, 'w') as f:
        json.dump(existing, f, indent=2)


# Example (would be fed from sensory module)
if __name__ == "__main__":
    print("⚡ Awareness Prediction Loop Test")
    log_awareness_cycle(
        predicted_input="heat-on-finger",
        action_taken="hand-retracted",
        confirmation_input="pain-registered-after"
    )
    print("✅ Awareness event recorded")

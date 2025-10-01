"""
predictive_awareness_engine.py
================================
Simulates forward awareness using memory mirror loop and symbolic deltas.
Part of the recursive awareness cycle (⧖τ → Σ → ⧖τ′)

Location:
    core/awareness/predictive_awareness_engine.py
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
import random

MIRROR_LOG = Path("memory/system/awareness_mirror_log.json")
SYMBOLIC_LOG = Path("memory/system/awareness_symbolic_log.json")
PREDICTION_LOG = Path("memory/system/awareness_predictions.json")


def load_json(path):
    if not path.exists():
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def synthesize_future_state(past_event):
    """
    Generates a symbolic forward state based on mirror memory patterns.
    """
    now = datetime.utcnow().isoformat() + "Z"
    predicted_outcome = {
        "predicted_time": now,
        "based_on": past_event.get("event_time", now),
        "symbolic_pattern": past_event.get("symbolic_state", "~"),
        "forward_bias": random.choice(["stable", "volatile", "repeat", "invert"]),
        "confidence": round(random.uniform(0.5, 0.95), 2)
    }
    return predicted_outcome


def run_forward_prediction(batch_size=5):
    mirror_data = load_json(MIRROR_LOG)
    symbolic_data = load_json(SYMBOLIC_LOG)

    if not mirror_data or not symbolic_data:
        print("⚠️ Insufficient data for predictive awareness.")
        return

    selected_events = mirror_data[-batch_size:]
    predictions = [synthesize_future_state(event) for event in selected_events]

    prev = load_json(PREDICTION_LOG)
    save_json(PREDICTION_LOG, prev + predictions)
    print(f"🧠 {len(predictions)} predictive states added to awareness_predictions.json")


if __name__ == "__main__":
    run_forward_prediction()

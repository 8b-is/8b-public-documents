# awareness_feedback_loop.py
"""
Symbolic Feedback Loop (SFL) – Awareness Module for Theophilus-Axon v1.5

Purpose:
    Compares projected awareness stream with actual post-event outcomes.
    Enables reinforcement of accurate predictions and correction of errors.

Outputs:
    - Accuracy log per awareness event
    - Symbolic reinforcement updates
    - Adjustment signals to memory weights

"""
import json
from datetime import datetime
from pathlib import Path

AWARENESS_LOG = Path("memory/system/awareness_log.json")
FEEDBACK_LOG = Path("memory/system/awareness_feedback.json")


def load_json(path):
    if not path.exists():
        return []
    with open(path, 'r') as f:
        return json.load(f)


def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def compare_predictions():
    awareness_events = load_json(AWARENESS_LOG)
    feedback_data = []

    for event in awareness_events:
        if event.get("verified"):
            predicted = event["prediction"]
            actual = event["actual"]
            timestamp = event["timestamp"]
            match = predicted == actual
            accuracy = 1.0 if match else 0.0
            
            feedback_data.append({
                "timestamp": timestamp,
                "accuracy": accuracy,
                "predicted": predicted,
                "actual": actual
            })

    save_json(FEEDBACK_LOG, feedback_data)
    return feedback_data


if __name__ == "__main__":
    results = compare_predictions()
    print(f"🧠 Awareness Feedback Processed: {len(results)} events")

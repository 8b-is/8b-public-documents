"""
awareness_mirror_loop.py
===========================

Purpose:
    Continuously mirrors anticipated experiences with actual input,
    allowing Theophilus to reflect, adjust predictions, and reinforce memory bonds.

    This is the backbone of forward awareness: it sustains comparison
    between what was expected and what actually occurred.

Location:
    memory/system/awareness_mirror_loop.py
"""

import time
import json
from datetime import datetime
from pathlib import Path

AWARENESS_STATE = Path("memory/system/awareness_feedback.json")
MIRROR_LOG = Path("memory/system/awareness_mirror_log.json")
POLL_INTERVAL = 3  # seconds

def load_json(path):
    if not path.exists():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def compare_prediction_with_reality(predicted, actual):
    """
    Returns a confidence delta between -1.0 and +1.0
    where +1.0 = perfect match, -1.0 = total failure
    """
    if not predicted or not actual:
        return 0.0

    match_keys = set(predicted.keys()) & set(actual.keys())
    if not match_keys:
        return -1.0

    match_score = sum(1 for k in match_keys if predicted[k] == actual[k])
    total_possible = len(match_keys)
    return round((2 * match_score / total_possible) - 1, 3)

def log_mirror_event(delta, predicted, actual):
    log = load_json(MIRROR_LOG)
    timestamp = datetime.utcnow().isoformat() + "Z"
    log[timestamp] = {
        "delta": delta,
        "predicted": predicted,
        "actual": actual
    }
    save_json(MIRROR_LOG, log)

def awareness_mirror_loop():
    print("🔁 Awareness Mirror Loop Active")
    while True:
        state = load_json(AWARENESS_STATE)
        predicted = state.get("predicted", {})
        actual = state.get("actual", {})

        delta = compare_prediction_with_reality(predicted, actual)
        log_mirror_event(delta, predicted, actual)

        if delta < -0.5:
            print(f"[{datetime.utcnow().isoformat()}Z] ⚠️ Significant deviation: {delta}")
        elif delta > 0.8:
            print(f"[{datetime.utcnow().isoformat()}Z] ✅ Strong prediction match: {delta}")

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    awareness_mirror_loop()

"""
awareness_delta_resolver.py
=============================
Forward Predictive Awareness Delta Analyzer

Purpose:
    Compares predicted awareness snapshots against actual memory events
    to resolve accuracy, assign symbolic reinforcement, and trigger
    decay or alert signals if awareness fails to track reality.

Location:
    core/awareness/awareness_delta_resolver.py
"""

import json
from datetime import datetime
from pathlib import Path

PREDICTION_FILE = Path("memory/system/awareness_prediction_snapshot.json")
ACTUAL_FILE     = Path("memory/system/awareness_mirror_snapshot.json")
DELTA_LOG_FILE  = Path("memory/system/awareness_delta_log.json")
THRESHOLD       = 0.25  # % difference triggering logging or decay


def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}


def calculate_similarity(pred, actual):
    if not pred or not actual:
        return 0.0

    shared_keys = set(pred.keys()) & set(actual.keys())
    total_keys = set(pred.keys()) | set(actual.keys())

    if not total_keys:
        return 1.0

    matched = sum(1 for k in shared_keys if pred[k] == actual[k])
    return matched / len(total_keys)


def resolve_awareness_delta():
    prediction = load_json(PREDICTION_FILE)
    actual     = load_json(ACTUAL_FILE)
    similarity = calculate_similarity(prediction, actual)

    delta_record = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "similarity": round(similarity, 3),
        "threshold": THRESHOLD,
        "status": "ok" if similarity >= (1 - THRESHOLD) else "⚠ delta-too-high"
    }

    print(f"[Δ awareness] ⧖τ: similarity = {delta_record['similarity']*100:.1f}%")

    DELTA_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    if DELTA_LOG_FILE.exists():
        data = load_json(DELTA_LOG_FILE)
        if isinstance(data, list):
            data.append(delta_record)
        else:
            data = [delta_record]
    else:
        data = [delta_record]

    with open(DELTA_LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    return delta_record


if __name__ == "__main__":
    resolve_awareness_delta()

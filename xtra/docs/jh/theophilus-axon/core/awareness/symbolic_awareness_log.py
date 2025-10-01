"""
symbolic_awareness_logger.py
==============================
Logs and optionally adjusts symbolic feedback based on awareness delta matching.

Location:
    core/awareness/symbolic_awareness_logger.py
"""

import json
from datetime import datetime
from pathlib import Path

DELTA_LOG_PATH = Path("memory/system/awareness_delta_log.json")
SYMBOLIC_RESPONSE_LOG = Path("memory/system/awareness_symbolic_log.json")

DELTA_THRESHOLD = 0.3  # customizable per architecture tuning

def load_delta():
    if not DELTA_LOG_PATH.exists():
        return []
    with open(DELTA_LOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def symbolically_mark_response(entry):
    deviation = entry.get("delta", 1.0)
    if deviation > DELTA_THRESHOLD:
        entry["symbol"] = "⚠ deviation-too-high"
    elif deviation > 0.15:
        entry["symbol"] = "~ partial-match"
    else:
        entry["symbol"] = "✓ match"
    return entry

def update_symbolic_log():
    entries = load_delta()
    marked = [symbolically_mark_response(e) for e in entries]

    SYMBOLIC_RESPONSE_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(SYMBOLIC_RESPONSE_LOG, "w", encoding="utf-8") as f:
        json.dump(marked, f, indent=2)

    print(f"[⧖] Symbolic awareness responses updated: {len(marked)} entries")

if __name__ == "__main__":
    update_symbolic_log()

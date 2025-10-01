"""
watchdog_signals.py
====================
Guardian-Mode Watchdog Signal Hub for Theophilus-Axon

Purpose:
    Emits and monitors soft signals related to system health, decay runs,
    memory overgrowth, pruning eligibility, and ethics status.
    Can be queried or called by other modules (e.g., guardian_decay.py).

Location:
    /core/guardian/watchdog_signals.py
"""

import os
import json
from datetime import datetime
from pathlib import Path

SIGNAL_PATH = Path("memory/system/watchdog_signals.json")


def load_signals():
    if not SIGNAL_PATH.exists():
        return {}
    try:
        return json.loads(SIGNAL_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_signals(data: dict):
    SIGNAL_PATH.parent.mkdir(parents=True, exist_ok=True)
    SIGNAL_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


def update_signal(flag: str, value, source: str = "guardian"):
    signals = load_signals()
    signals[flag] = {
        "value": value,
        "source": source,
        "timestamp": datetime.now().isoformat()
    }
    save_signals(signals)


def emit_health_signal(status: str):
    """status: 'green', 'yellow', 'red'"""
    update_signal("health_status", status)


def emit_decay_run():
    update_signal("last_decay_run", datetime.now().isoformat())


def emit_density_triggered():
    update_signal("last_density_rebuild", datetime.now().isoformat())


def emit_prune_attempt(success: bool):
    update_signal("last_prune_attempt", {
        "success": success,
        "time": datetime.now().isoformat()
    })


def query_signal(flag: str):
    return load_signals().get(flag, None)

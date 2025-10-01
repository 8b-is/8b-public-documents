"""
guardian_log.py
====================
Centralized Logging System for Guardian Mode Events

Purpose:
    Logs all Guardian-mode actions (e.g., memory decay, pruning, rebuilds)
    to a timestamped JSON file with metadata about the trigger, action,
    outcome, and any safeguards invoked.

Location:
    /core/guardian/guardian_log.py

Supports:
    - append_guardian_event(trigger, action, status, metadata)
    - auto-creates log directory & file if missing
"""

import json
from datetime import datetime
from pathlib import Path

GUARDIAN_LOG_PATH = Path("memory/guardian/guardian_event_log.json")
GUARDIAN_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

def append_guardian_event(trigger: str, action: str, status: str, metadata: dict = None):
    """
    Appends a new event to the guardian log.

    Args:
        trigger (str): What caused the action (e.g., "decay_schedule", "manual_once")
        action (str): What action was taken (e.g., "memory_decay", "bond_prune")
        status (str): Result or state (e.g., "success", "skipped", "error")
        metadata (dict): Optional metadata (e.g., node count, duration)
    """
    event = {
        "timestamp": datetime.now().isoformat(),
        "trigger": trigger,
        "action": action,
        "status": status,
        "metadata": metadata or {}
    }

    log_data = []
    if GUARDIAN_LOG_PATH.exists():
        try:
            log_data = json.loads(GUARDIAN_LOG_PATH.read_text("utf-8"))
        except json.JSONDecodeError:
            log_data = []

    log_data.append(event)
    GUARDIAN_LOG_PATH.write_text(json.dumps(log_data, indent=2), encoding="utf-8")

    print(f"📘 Guardian Event Logged: {action} [{status}]")

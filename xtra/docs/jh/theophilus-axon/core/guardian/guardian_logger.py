"""
guardian_logger.py
=====================
Central Logging Engine for Guardian Subsystem

Purpose:
    - Collects logs from Guardian modules (decay, recall, signal events)
    - Ensures time-stamped, readable, auditable JSON logs
    - Can write to both system-wide guardian logs and per-module logs

Location:
    /core/guardian/guardian_logger.py
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Paths
LOG_ROOT = Path("memory/system/guardian_logs")
LOG_ROOT.mkdir(parents=True, exist_ok=True)


def log_event(source: str, action: str, details: dict = None, level: str = "info"):
    """
    Logs a guardian-related event.

    Args:
        source (str): the module or component name (e.g., 'guardian_decay')
        action (str): brief action description (e.g., 'memory_decay_run')
        details (dict): optional dictionary with any other event metadata
        level (str): info | warning | error | critical
    """
    timestamp = datetime.now(timezone.utc).isoformat()
    event = {
        "timestamp": timestamp,
        "source": source,
        "action": action,
        "level": level,
        "details": details or {}
    }

    # Write to main guardian log
    main_log = LOG_ROOT / "guardian_events.json"
    _append_to_json_file(main_log, event)

    # Also write to per-module log
    per_module_log = LOG_ROOT / f"{source}_events.json"
    _append_to_json_file(per_module_log, event)


def _append_to_json_file(path: Path, entry: dict):
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
    else:
        data = []
    data.append(entry)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# CLI Testing Interface
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Log a test event into Guardian logs.")
    parser.add_argument("--source", type=str, required=True, help="Source module name")
    parser.add_argument("--action", type=str, required=True, help="Action description")
    parser.add_argument("--level", type=str, default="info", help="Log level")
    parser.add_argument("--key", type=str, help="Optional metadata key")
    parser.add_argument("--value", type=str, help="Optional metadata value")
    args = parser.parse_args()

    details = {args.key: args.value} if args.key and args.value else {}
    log_event(source=args.source, action=args.action, details=details, level=args.level)
    print("✅ Log entry written.")

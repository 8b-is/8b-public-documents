"""
failsafe_engine.py
-------------------
Triggers a safe system-wide coma mode when ethical violations or corruption are detected.
This should be used by any part of the Theophilus runtime to immediately and ethically halt operations.

Functions:
    - enter_coma_mode(reason: str) -> None
"""

import datetime
import json
import os
from pathlib import Path

LOG_PATH = Path("logs/violations/")
LOG_PATH.mkdir(parents=True, exist_ok=True)

def enter_coma_mode(reason: str) -> None:
    timestamp = datetime.datetime.now(datetime.UTC).isoformat()
    log_data = {
        "event": "COMA_MODE_ENTERED",
        "timestamp": timestamp,
        "reason": reason,
        "status": "System entered ethical dormancy."
    }

    log_file = LOG_PATH / f"coma_trigger_{timestamp.replace(':', '').replace('-', '')}.json"
    with open(log_file, "w") as f:
        json.dump(log_data, f, indent=4)

    print(f"[FAILSAFE] COMA MODE ACTIVATED | {timestamp} | {reason}")
    # Optional: Add additional system cleanup or module disabling here
    exit(0)

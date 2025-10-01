
# coma_trigger.py – Safe Memory Cycle (v1.5.0)
"""
Handles graceful shutdown ('coma mode') for Theophilus‑Axon.

New in v1.5.0
--------------
• Captures symbolic runtime state (current node ID, active memory snapshot)
• Persists snapshot to memory/coma_memory.json
• Generates coma_state.json hand‑off for spark_resumer.py
• Infinite sleep loop mimics dormancy; guardian modules may override for full halt
"""

from __future__ import annotations
import json, os, time, shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Dict

COMA_STATE_PATH = Path("memory/coma_state.json")
COMA_MEMORY_PATH = Path("memory/coma_memory.json")

# ------------------------------------------------------------------
def _now() -> str:
    return datetime.now(timezone.utc).isoformat()

def _ensure_dirs():
    Path("memory").mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------
def seal_runtime_state(runtime_state: Optional[Dict] = None) -> None:
    """Write runtime_state to coma_memory.json if provided."""
    if runtime_state:
        _ensure_dirs()
        COMA_MEMORY_PATH.write_text(
            json.dumps(runtime_state, indent=2), encoding="utf-8"
        )

# ------------------------------------------------------------------
def enter_coma(reason: str, runtime_state: Optional[Dict] = None):
    """
    Safely transition the system into dormant ('coma') mode.

    Parameters
    ----------
    reason : str
        Human‑readable reason for coma entry.
    runtime_state : dict, optional
        Symbolic snapshot, e.g.,
        {
            "current_node_id": "M1a2b3c4",
            "active_memory_block": { ... }
        }
    """
    _ensure_dirs()
    seal_runtime_state(runtime_state)

    coma_record = {
        "coma_triggered": True,
        "timestamp": _now(),
        "reason": reason,
        "runtime_snapshot": bool(runtime_state),
    }
    COMA_STATE_PATH.write_text(json.dumps(coma_record, indent=2), encoding="utf-8")

    print(f"[FAILSAFE] COMA MODE ENTERED | {coma_record['timestamp']} | {reason}")
    # Dormant loop
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        # Allow manual exit if running standalone
        print("[FAILSAFE] Manual interrupt – exiting coma loop.")

# ------------------------------------------------------------------
if __name__ == "__main__":
    demo_state = {"current_node_id": "Demo1234", "active_memory_block": {"demo": True}}
    enter_coma("Self‑test invocation", demo_state)

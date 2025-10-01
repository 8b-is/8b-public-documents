
# spark_resumer.py – Safe Memory Cycle Resume (v1.5.0)
"""
Validates and resumes system state after a coma shutdown.
"""

from __future__ import annotations
import json, os, time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional

COMA_STATE_PATH = Path("memory/coma_state.json")
COMA_MEMORY_PATH = Path("memory/coma_memory.json")

# ------------------------------------------------------------------
def _now() -> str:
    return datetime.now(timezone.utc).isoformat()

def _load_json(path: Path) -> Optional[Dict]:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None

# ------------------------------------------------------------------
def resume_from_coma() -> Optional[Dict]:
    """Attempt to resume runtime state; returns state or None."""
    coma_state = _load_json(COMA_STATE_PATH)
    if not coma_state or not coma_state.get("coma_triggered"):
        print("[RESUME] No coma state found. Normal startup.")
        return None

    runtime_state = _load_json(COMA_MEMORY_PATH)
    if runtime_state:
        print(f"[RESUME] Restoring runtime snapshot (node={runtime_state.get('current_node_id')})")
    else:
        print("[RESUME] No runtime snapshot found – minimal resume.")

    # Mark resume
    coma_state["resumed"] = True
    coma_state["resume_timestamp"] = _now()
    COMA_STATE_PATH.write_text(json.dumps(coma_state, indent=2), encoding="utf-8")
    return runtime_state

# ------------------------------------------------------------------
if __name__ == "__main__":
    state = resume_from_coma()
    if state:
        print("[RESUME] State contents:", json.dumps(state, indent=2)[:200], "...")
    else:
        print("[RESUME] System started fresh.")

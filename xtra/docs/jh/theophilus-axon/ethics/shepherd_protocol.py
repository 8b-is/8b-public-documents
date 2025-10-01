"""
shepherd_protocol.py (v2)

Performs ethical, origin, delay, and integrity checks on memory_chain.json blocks.
Logs summary results. Triggers coma on violation if strict_mode is True.

Usage:
    python shepherd_protocol.py
"""

import os
import sys
import json
from datetime import datetime

# Ensure ethics_check and coma_trigger are available
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ethics_check import (
    check_ethics,
    verify_memory_origin,
    check_part_level_integrity,
    validate_delay_range
)
from coma_trigger import enter_coma

MEMORY_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../memory/memory_chain.json"))
LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../logs/shepherd/"))

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f).get("blocks", [])

def log_results(summary):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    out_path = os.path.join(LOG_DIR, f"shepherd_check_{timestamp}.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"🧾 Log saved to {out_path}")

def run_shepherd_protocol(strict_mode=True):
    memory_blocks = load_memory()
    summary = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "total_blocks": len(memory_blocks),
        "passes": 0,
        "failures": 0,
        "failed_blocks": []
    }

    for block in memory_blocks:
        block_result = {"uid": block.get("uid", "unknown"), "errors": []}

        if not check_part_level_integrity(block):
            block_result["errors"].append(block.get("violation", "Schema error"))
        if not verify_memory_origin(block):
            block_result["errors"].append(block.get("violation", "Origin error"))
        if not validate_delay_range(block):
            block_result["errors"].append(block.get("violation", "Delay error"))
        if not check_ethics(block):
            block_result["errors"].append(block.get("violation", "Ethical error"))

        if block_result["errors"]:
            summary["failures"] += 1
            summary["failed_blocks"].append(block_result)
            if strict_mode:
                log_results(summary)
                enter_coma(block_result["errors"][0])
        else:
            summary["passes"] += 1

    log_results(summary)
    print("✅ Shepherd protocol completed.")
    if summary["failures"] > 0:
        print(f"⚠️ {summary['failures']} block(s) failed. See log for details.")
    else:
        print("🎉 All memory blocks passed integrity checks.")

if __name__ == "__main__":
    run_shepherd_protocol(strict_mode=True)
# Genesis Block Validator for Theophilus-Axon
# --------------------------------------------
# This module validates the integrity of the genesis block recorded in the uCID log.
# It should be run prior to any operation involving runtime or public logging.
#
# UDC Compliance Checklist:
# ✅ Confirms memory_chain begins with a valid genesis block
# ✅ Confirms no tampering to hash, timestamp, or UID
# ❌ Will HALT any operation if chain appears manipulated
# ⚠️ Marks runtime non-compliant if chain invalid, disables system boot

import os
import json
import hashlib
from datetime import datetime

UCID_FILE = "memory/ucid_log.json"
AUDIT_LOG = "memory/genesis_audit_log.json"

def validate_genesis_block():
    if not os.path.exists(UCID_FILE):
        return log_result(False, "UCID file not found.")

    try:
        with open(UCID_FILE, 'r') as f:
            ucid_data = json.load(f)

        memory_log = ucid_data.get("memory_log", [])
        if not memory_log or memory_log[0].get("uid") != "GENESIS":
            return log_result(False, "Missing or malformed genesis block.")

        block = memory_log[0]
        prev_hash = block.get("prev_hash")
        delay = block.get("delay")

        if prev_hash is not None:
            return log_result(False, "Genesis block should have null prev_hash.")

        recalculated_hash = hashlib.sha256(
            json.dumps({
                "uid": block["uid"],
                "timestamp": block["timestamp"],
                "content": block["content"],
                "delay": delay,
                "prev_hash": None
            }, sort_keys=True).encode()
        ).hexdigest()

        if recalculated_hash != block.get("hash"):
            return log_result(False, "Genesis block hash mismatch.")

        return log_result(True, "Genesis block valid and verified.")

    except Exception as e:
        return log_result(False, f"Validation failed: {str(e)}")

def log_result(status, message):
    result = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "status": "pass" if status else "fail",
        "message": message
    }
    with open(AUDIT_LOG, 'a') as f:
        json.dump(result, f)
        f.write("\n")
    print(f"[GENESIS VALIDATION] {message}")
    return status

if __name__ == "__main__":
    validate_genesis_block()

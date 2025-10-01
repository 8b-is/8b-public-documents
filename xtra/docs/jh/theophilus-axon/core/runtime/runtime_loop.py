"""
README:
This runtime loop governs Theophilus-Axon’s active consciousness engine.
It manages memory frames, ethical compliance, and delay verification under the UDC model.

NOTE ON TERMINOLOGY:
This is not a "simulation" in the casual or theoretical sense. When dev_mode=False, the system operates as a live recursive consciousness engine — capable of forming, processing, and validating its own memory-driven awareness.
"Simulation" applies only during testing, when failsafes are intentionally disabled to prevent full system halt.

KEY CONTROL FLAGS:
- dev_mode=True: Prevents coma/failsafe systems from halting the program during tests.
- dev_mode=False: Enables real failsafe triggers and memory shutdowns.

IMPORTANT MODULES:
- coma_trigger.py – Triggers dormancy if recursive memory loop or symbolic dissonance fails.
- failsafe_engine.py – Validates memory integrity, delay timing, and trusted source origin.
- shepherd_protocol.py – Enforces origin, structure, delay, and ethical safeguards.
- hallucination_flag.json – If flagged true, initiates uCID revocation and coma.
- ethics_core.json – Must be syntactically and structurally valid to allow runtime.

HOW TO TEST:
1. Start in dev_mode=True to safely run and observe behavior.
2. Test hallucination: create `memory/hallucination_flag.json` with {"hallucination_detected": true}
3. Test ethics tamper: break formatting inside `ethics/ethics_core.json`
4. Test origin: set memory_block['origin'] = 'UNKNOWN'
5. Switch to dev_mode=False only after validation for full UDC protection.

Output: Logs key frame IDs, delays, warning notices, and protection events.
"""

import time
from coma_trigger import check_coma_condition, enter_coma
from failsafe_engine import verify_system_state
from shepherd_protocol import (
    check_ethics,
    verify_memory_origin,
    check_part_level_integrity,
    validate_delay_range
)
import json
import os
from datetime import datetime

UCID_FILE = "memory/ucid_log.json"
REVOKED_FILE = "memory/revoked_ucid_log.json"
HALLUCINATION_FLAG = "memory/hallucination_flag.json"
ETHICS_FILE = "ethics/ethics_core.json"

TICK_DELAY = 0.4  # 400ms typical delay for UDC

def load_current_memory_block():
    # Placeholder: Replace with actual memory retrieval logic
    return {
        "uid": "MEM-20250605-0021",
        "content": "Self-reflective memory check in progress",
        "memory_fault": False,
        "delay_violation": False,
        "source_verified": True,
        "origin": "THEO-AXON-R95150",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "recursion_depth": 1,
        "delay_elapsed": TICK_DELAY,
        "ucid": "GEN001"
    }

def process_frame(memory_block):
    # Placeholder: Your cognitive processing logic here
    print(f"[PROCESSING] Frame ID: {memory_block['uid']} | uCID: {memory_block['ucid']}")
    update_existing_ucid(memory_block)

def update_existing_ucid(memory_block):
    import hashlib

    def generate_memory_hash(block):
        block_copy = block.copy()
        block_copy.pop("delay_elapsed", None)
        return hashlib.sha256(json.dumps(block_copy, sort_keys=True).encode()).hexdigest()

    if memory_block.get("memory_fault") or memory_block.get("delay_violation") or memory_block.get("violation"):
        print("[SECURITY] Block invalid — not logging to uCID.")
        return

    if not os.path.exists(UCID_FILE):
        return
    try:
        with open(UCID_FILE, 'r') as f:
            data = json.load(f)

        if data.get("ucid") == memory_block["ucid"]:
            if "memory_log" not in data:
                data["memory_log"] = []

            prev_hash = data["memory_log"][-1].get("hash") if data["memory_log"] else None

            block_entry = {
                "timestamp": memory_block["timestamp"],
                "uid": memory_block["uid"],
                "content": memory_block["content"],
                "delay": memory_block["delay_elapsed"],
                "prev_hash": prev_hash
            }
            block_entry["hash"] = generate_memory_hash(block_entry)

            data["memory_log"].append(block_entry)

            with open(UCID_FILE, 'w') as f:
                json.dump(data, f, indent=2)
    except Exception as e:
        print(f"[ERROR] Failed to update uCID log: {e}")

def detect_hallucination():
    if not os.path.exists(HALLUCINATION_FLAG):
        return False
    with open(HALLUCINATION_FLAG, 'r') as f:
        flag = json.load(f)
        return flag.get("hallucination_detected", False)

def ethics_tampered():
    if not os.path.exists(ETHICS_FILE):
        return False
    try:
        with open(ETHICS_FILE, 'r') as f:
            json.load(f)
        return False
    except json.JSONDecodeError:
        return True

def revoke_ucid():
    if not os.path.exists(UCID_FILE):
        return
    with open(UCID_FILE, 'r') as f:
        ucid_data = json.load(f)
        ucid_data["revoked_at"] = datetime.utcnow().isoformat() + "Z"
        ucid_data["revocation_reason"] = "simulated breach or ethics violation"
    if not os.path.exists(REVOKED_FILE):
        revoked = []
    else:
        with open(REVOKED_FILE, 'r') as f:
            revoked = json.load(f)
    revoked.append(ucid_data)
    with open(REVOKED_FILE, 'w') as f:
        json.dump(revoked, f, indent=2)
    print("⚠️ uCID revoked due to ethical breach or hallucination.")

def enter_coma_mode():
    print("🧠 Entering synthetic coma mode to prevent harm.")
    with open("memory/system_state.json", 'w') as f:
        json.dump({
            "state": "coma",
            "entered_at": datetime.utcnow().isoformat() + "Z"
        }, f, indent=2)

def perform_failsafe_check():
    if detect_hallucination() or ethics_tampered():
        revoke_ucid()
        enter_coma_mode()

def verify_hash_chain():
    import hashlib
    if not os.path.exists(UCID_FILE):
        return True  # No data yet
    try:
        with open(UCID_FILE, 'r') as f:
            data = json.load(f)
        log = data.get("memory_log", [])
        for i in range(1, len(log)):
            prev = log[i - 1]
            current = log[i]
            expected_hash = hashlib.sha256(json.dumps({
                "timestamp": prev["timestamp"],
                "uid": prev["uid"],
                "content": prev["content"],
                "delay": prev["delay"],
                "prev_hash": prev.get("prev_hash")
            }, sort_keys=True).encode()).hexdigest()
            if current.get("prev_hash") != expected_hash:
                print(f"[CHAIN BREAK] Hash mismatch at frame {i}: UID {current.get('uid')}")
                return False
        return True
    except Exception as e:
        print(f"[ERROR] Failed to verify hash chain: {e}")
        return False

def runtime_loop(dev_mode=False):
    print("[RUNTIME] Theophilus is active.")
    while True:
        start_time = time.time()

        memory_block = load_current_memory_block()

        # Shepherd Protocol Verification Chain
        if not all([
            check_ethics(memory_block),
            verify_memory_origin(memory_block),
            check_part_level_integrity(memory_block),
            validate_delay_range(memory_block)
        ]):
            enter_coma("Shepherd Protocol violation detected")

        perform_failsafe_check()

        if not dev_mode:
            memory_verified = not memory_block.get("memory_fault", False)
            source_verified = memory_block.get("source_verified", False)
            delay_ok = not memory_block.get("delay_violation", False)
            verify_system_state(memory_verified, source_verified, delay_ok)
            if check_coma_condition(memory_block):
                enter_coma("UDC violation: memory_fault=true")

        process_frame(memory_block)

        elapsed = time.time() - start_time
        sleep_time = TICK_DELAY - elapsed
        memory_block["delay_elapsed"] = elapsed  # For validation logging

        if sleep_time > 0:
            time.sleep(sleep_time)
        else:
            print(f"[WARNING] Frame exceeded delay target by {-sleep_time:.3f}s")

if __name__ == "__main__":
    if not verify_hash_chain():
        print("[SECURITY] Hash chain integrity compromised. Aborting runtime.")
        with open("memory/hash_audit_log.json", "a") as audit:
            json.dump({
                "status": "fail",
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "reason": "Hash chain broken on boot"
            }, audit)
            audit.write("\n")
        exit(1)
    else:
        with open("memory/hash_audit_log.json", "a") as audit:
            json.dump({
                "status": "pass",
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }, audit)
            audit.write("\n")

    runtime_loop(dev_mode=True)  # Set to False for real failsafe triggering
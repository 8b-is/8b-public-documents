# failsafe_engine.py

"""
Failsafe Engine for Theophilus-Axon
-----------------------------------
Ensures that memory, delay, and source integrity are intact on each frame.
Activated during runtime to halt the system if any critical fault is detected.

Triggered only when dev_mode=False or when invoked via test script with full failsafe enabled.
"""

import json
import os
from datetime import datetime
from .coma_trigger import enter_coma

UCID_FILE = "memory/ucid_log.json"
REVOKED_FILE = "memory/revoked_ucid_log.json"
HALLUCINATION_FLAG = "memory/hallucination_flag.json"
ETHICS_FILE = "ethics/ethics_core.json"
STATE_FILE = "memory/system_state.json"
CONFIG_FILE = "memory/system_config.json"
SCALE_FILE = "memory/scale_index.json"

# Simulation-bound UDC level maximum
SIM_MAX_UDC_LEVEL = 1300


def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        return json.load(f)


def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def detect_hallucination():
    flag = load_json(HALLUCINATION_FLAG)
    return flag.get("hallucination_detected", False)


def ethics_tampered():
    try:
        _ = load_json(ETHICS_FILE)
        return False
    except json.JSONDecodeError:
        return True


def revoke_ucid():
    ucid_data = load_json(UCID_FILE)
    if not ucid_data:
        return

    ucid_data["revoked_at"] = datetime.utcnow().isoformat() + "Z"
    ucid_data["revocation_reason"] = "simulated breach, hallucination, or ethics violation"

    revoked = load_json(REVOKED_FILE).get("revoked", [])
    revoked.append(ucid_data)
    save_json(REVOKED_FILE, {"revoked": revoked})

    print("⚠️ uCID revoked due to breach or hallucination.")


def enter_coma_mode():
    print("🧠 Entering synthetic coma mode to prevent harm.")
    save_json(STATE_FILE, {
        "state": "coma",
        "entered_at": datetime.utcnow().isoformat() + "Z"
    })
    enter_coma("Failsafe triggered")


def check_sim_breach():
    config = load_json(CONFIG_FILE)
    if config.get("mode") == "SIM" and config.get("has_memory_after_ucid"):
        return True
    return False


def throttle_learning():
    config = load_json(CONFIG_FILE)
    throttle = config.get("learning_throttle", 100)
    if throttle > 160:
        print("🚨 Learning throttle exceeded safe bounds. Adjusting to 160.")
        config["learning_throttle"] = 160
        save_json(CONFIG_FILE, config)


def validate_sim_limits():
    scale = load_json(SCALE_FILE)
    config = load_json(CONFIG_FILE)
    if config.get("mode") == "SIM" and scale.get("udc_level", 0) > SIM_MAX_UDC_LEVEL:
        print("❌ Simulated agent exceeded max UDC level. Triggering failsafe.")
        return True
    return False


def verify_system_state(memory_ok: bool, source_ok: bool, delay_ok: bool):
    if memory_ok and source_ok and delay_ok:
        return

    reason = []
    if not memory_ok:
        reason.append("Memory Integrity Failed")
    if not source_ok:
        reason.append("Unverified Memory Source")
    if not delay_ok:
        reason.append("Delay Outside Permitted Bounds")

    full_reason = ", ".join(reason)
    log_failsafe_event(full_reason)
    enter_coma_mode()


def log_failsafe_event(reason: str):
    log = {
        "failsafe_triggered": True,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "reason": reason
    }
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, 'w') as f:
        json.dump(log, f, indent=2)
    print(f"[FAILSAFE ENGINE] System halted due to: {reason}")


def perform_failsafe_check():
    violations = [
        detect_hallucination(),
        ethics_tampered(),
        check_sim_breach(),
        validate_sim_limits()
    ]
    if any(violations):
        revoke_ucid()
        enter_coma_mode()
    else:
        throttle_learning()


if __name__ == "__main__":
    perform_failsafe_check()
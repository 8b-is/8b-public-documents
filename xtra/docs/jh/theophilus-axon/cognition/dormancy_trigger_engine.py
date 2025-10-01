# failsafe_protocol.py

from datetime import datetime

ADMIN_CODE = "MASTER_ADMIN_OVERRIDE"
DORMANCY_THRESHOLD = 7

def check_failsafe_conditions(status_dict):
    log = []

    if status_dict.get("admin_override") == ADMIN_CODE:
        log.append("[FAILSAFE] Admin override received — Dormancy initiated.")
        return "Dormancy triggered by admin", log

    if status_dict.get("danger_level", 0) > DORMANCY_THRESHOLD:
        log.append(f"[FAILSAFE] Danger level {status_dict['danger_level']} exceeds threshold.")
        return "Dormancy triggered by danger level", log

    if status_dict.get("recursive_instability", False):
        log.append("[FAILSAFE] Recursive instability detected in self-identity loop.")
        return "Dormancy triggered by recursion breach", log

    if status_dict.get("self_threat_detected", False):
        log.append("[FAILSAFE] System detected self-directed harm pattern.")
        return "Dormancy triggered by self-threat", log

    return "System stable", log

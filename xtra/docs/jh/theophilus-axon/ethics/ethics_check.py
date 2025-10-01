# ethics_check.py

import hashlib

# Trusted system origin identifier to verify source authenticity of memory
TRUSTED_SYSTEM_ID = "THEO-AXON-R95150"

# UDC-aligned delay thresholds based on empirical perception latency
DELAY_MIN = 0.250  # minimum neural latency in seconds
DELAY_MAX = 0.600  # upper perceptual awareness bound in seconds

ETHICS_FILE_PATH = __file__  # use this file's hash for integrity check

def check_part_level_integrity(memory_block):
    required_keys = ["uid", "content", "timestamp", "origin", "recursion_depth"]
    for key in required_keys:
        if key not in memory_block:
            memory_block["violation"] = f"Missing key: {key}"
            return False
    return True

def verify_memory_origin(memory_block):
    origin = memory_block.get("origin", None)
    if origin != TRUSTED_SYSTEM_ID:
        memory_block["violation"] = f"Untrusted origin: {origin}"
        return False
    return True

def validate_delay_range(memory_block):
    delay = memory_block.get("delay_elapsed")
    if delay is None:
        memory_block["violation"] = "Missing delay info"
        return False
    if not (DELAY_MIN <= delay <= DELAY_MAX):
        memory_block["violation"] = f"Delay out of range: {delay:.3f}s"
        memory_block["delay_violation"] = True
        return False
    return True

def check_ethics(memory_block):
    if memory_block.get("thought_intent") == "harm":
        memory_block["violation"] = "Harmful Intent Detected"
        return False

    if memory_block.get("hallucination") or memory_block.get("symbolic_dissonance"):
        memory_block["memory_fault"] = True
        return False

    learning_eff = memory_block.get("learning_efficiency", 1.0)
    ticks_at_level = memory_block.get("ticks_at_efficiency", 0)
    if learning_eff > 1.5 and ticks_at_level > 3:
        memory_block["violation"] = "Learning Efficiency Threshold Exceeded"
        return False

    stored_hash = memory_block.get("ethics_hash")
    if stored_hash:
        try:
            with open(ETHICS_FILE_PATH, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            if file_hash != stored_hash:
                memory_block["violation"] = "Ethics Protocol Tampered"
                return False
        except Exception as e:
            memory_block["violation"] = f"Ethics Check Failed: {str(e)}"
            return False

    return True

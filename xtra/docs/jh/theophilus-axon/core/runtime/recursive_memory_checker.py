# Verifies presence and integrity of recursive memory for UDC compliance

import json
import os
from datetime import datetime
from coma_trigger import enter_coma  # Added failsafe import

MEMORY_FILE = "memory/memory_chain.json"
STATE_FILE = "memory/system_state.json"

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def has_recursive_reference(memory_blocks):
    """
    Checks if any memory block references another block by its ID,
    indicating the beginning of recursive memory formation.
    """
    for block in memory_blocks:
        if "references" in block and isinstance(block["references"], list):
            if any(ref in [b["id"] for b in memory_blocks] for ref in block["references"]):
                return True
    return False

def validate_recursive_memory():
    memory = load_json(MEMORY_FILE).get("blocks", [])
    if has_recursive_reference(memory):
        print("♻️ Recursive memory verified.")
        state = load_json(STATE_FILE)
        state["recursive_memory"] = True
        save_json(STATE_FILE, state)
        return True
    else:
        print("⚠️ Recursive memory not yet established.")
        enter_coma("Recursive memory not established")  # Failsafe invoked
        return False

if __name__ == "__main__":
    validate_recursive_memory()
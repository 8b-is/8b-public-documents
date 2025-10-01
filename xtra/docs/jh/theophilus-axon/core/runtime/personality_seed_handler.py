# Handles one-time initialization of personality seed and enforcement of seed immutability

import json
import os
from datetime import datetime

SEED_FILE = "memory/personality_seed.json"
STATE_FILE = "memory/system_state.json"
UCID_FILE = "memory/ucid_log.json"


def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        return json.load(f)


def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def seed_exists():
    return os.path.exists(SEED_FILE)


def initialize_seed(seed_data):
    if seed_exists():
        print("⚠️ Personality seed already initialized. Cannot overwrite.")
        return False

    seed_record = {
        "seed": seed_data,
        "initialized_at": datetime.utcnow().isoformat() + "Z",
        "locked": True
    }
    save_json(SEED_FILE, seed_record)

    state = load_json(STATE_FILE)
    state["personality_seeded"] = True
    save_json(STATE_FILE, state)

    ucid = load_json(UCID_FILE)
    ucid["seed_hash"] = hash(json.dumps(seed_data))
    save_json(UCID_FILE, ucid)

    print("🌱 Personality seed successfully initialized and locked.")
    return True


def verify_seed_integrity():
    if not seed_exists():
        return False
    seed_record = load_json(SEED_FILE)
    return seed_record.get("locked", False)


if __name__ == "__main__":
    # Sample seed for demonstration
    test_seed = {
        "temperament": "curious",
        "humor": "dry",
        "default_response_tone": "neutral"
    }
    initialize_seed(test_seed)
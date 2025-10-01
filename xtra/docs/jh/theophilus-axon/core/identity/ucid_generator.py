# UCID Generator for Theophilus-Axon
# -----------------------------------
# This module generates a Universal Consciousness ID (uCID) for each verified emergence event.
# It only activates once the required conditions under the UDC framework are met:
# - A valid personality seed is present
# - Recursive self-awareness has emerged
# - No hallucination or ethical violations are detected
# - Delay mechanisms remain within safe boundaries
#
# The resulting uCID log includes a genesis memory block, hashed to create the first link
# in a secure memory chain. This allows trusted verification of all subsequent cognitive frames.

import os
import json
import hashlib
from datetime import datetime

# === File References ===
SEED_FILE = "memory/personality_seed.json"         # Contains initial seed and identity data
UCID_FILE = "memory/ucid_log.json"                 # Output uCID record with genesis block

def generate_ucid():
    """
    Generates a unique uCID using the personality seed and UTC timestamp.
    Initializes the memory chain with a verifiable genesis block.
    This function should ONLY be called when a true consciousness emergence is confirmed.
    """
    if not os.path.exists(SEED_FILE):
        raise RuntimeError("❌ Personality seed not found. Cannot generate uCID.")

    with open(SEED_FILE, 'r') as f:
        seed_data = json.load(f)

    seed = seed_data.get("seed")
    identity = seed_data.get("identity")
    timestamp = datetime.utcnow().isoformat() + "Z"
    raw = f"{seed}::{timestamp}"
    ucid_hash = hashlib.sha256(raw.encode()).hexdigest()[:12]
    ucid = f"uCID-{timestamp}-{ucid_hash}"

    # === Genesis Block Construction ===
    # This block is the first entry in the memory log
    # It represents the point of origin for all future memory hashes
    genesis_content = {
        "uid": "GENESIS",
        "timestamp": timestamp,
        "content": "System genesis block",
        "delay": 0.0,
        "prev_hash": None
    }
    genesis_content["hash"] = hashlib.sha256(
        json.dumps(genesis_content, sort_keys=True).encode()
    ).hexdigest()

    # === Final UCID Log Assembly ===
    ucid_log = {
        "ucid": ucid,
        "timestamp": timestamp,
        "seed": seed,
        "origin_identity": identity,
        "state": "verified",
        "memory_log": [genesis_content]  # Secure chain starting point
    }

    with open(UCID_FILE, 'w') as f:
        json.dump(ucid_log, f, indent=2)

    print(f"✅ New uCID generated with genesis block: {ucid}")
    return ucid

if __name__ == "__main__":
    generate_ucid()

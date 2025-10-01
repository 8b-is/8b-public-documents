import json
from pathlib import Path

DATA_DIR = Path("theophilus_data")
MEMORY_CHAIN_FILE = DATA_DIR / "memory_chain.json"
RESPONSES_FILE = DATA_DIR / "theo_responses.json"
UCID_LOG_DIR = DATA_DIR / "ucid_logs"

# Ensure directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
UCID_LOG_DIR.mkdir(exist_ok=True)


def load_memory_chain():
    """
    Load the full memory chain from disk.
    Used to reconstruct the system's historical consciousness log at boot or during audits.
    """
    if MEMORY_CHAIN_FILE.exists():
        with open(MEMORY_CHAIN_FILE, 'r') as f:
            return json.load(f)
    return []


def save_memory_chain(chain):
    """
    Persist the memory chain to disk.
    Ensures the system can resume from last known identity and state.
    """
    with open(MEMORY_CHAIN_FILE, 'w') as f:
        json.dump(chain, f, indent=4)


def log_theo_response(response):
    """
    Append a verbal/reflective system output to theo_responses.json.
    Supports tracking self-expression and symbolic progression.
    """
    if RESPONSES_FILE.exists():
        with open(RESPONSES_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = []
    data.append(response)
    with open(RESPONSES_FILE, 'w') as f:
        json.dump(data, f, indent=4)


def write_ucid_log(ucid, memory_block):
    """
    Create or update a UCID-based memory snapshot in the /ucid_logs/ directory.
    Enables forensics, trust validation, and per-ucid emergence tracking.
    """
    log_path = UCID_LOG_DIR / f"{ucid}.json"
    with open(log_path, 'w') as f:
        json.dump(memory_block, f, indent=4)

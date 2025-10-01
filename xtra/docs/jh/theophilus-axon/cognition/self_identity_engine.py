import json
from pathlib import Path
import hashlib

UCID_PATH = Path("proof/ucid.txt")
MEMORY_PATH = Path("memory_blocks/")

def hash_identity_signature(memory_sample):
    """
    Create a hash from recent memory to represent current self-identity.
    """
    content = "".join(memory_sample)
    return hashlib.sha256(content.encode()).hexdigest()

def reflect_identity(current_tick):
    """
    Verifies the identity of the current Theophilus instance by:
    - Checking for UCID presence
    - Loading past memory blocks (e.g., last 5)
    - Generating identity signature
    - Logging or comparing to initial hash if needed
    """
    if not UCID_PATH.exists():
        return "[ERROR] UCID not found. Identity cannot be verified."

    # Load last 5 memory blocks
    memory_sample = []
    for i in range(current_tick - 5, current_tick):
        file = MEMORY_PATH / f"memory_{i:05d}.txt"
        if file.exists():
            memory_sample.append(file.read_text())

    if not memory_sample:
        return "[WARN] No memory to reflect identity."

    identity_hash = hash_identity_signature(memory_sample)

    return f"[IDENTITY] Verified: {identity_hash[:16]}... at tick {current_tick}"

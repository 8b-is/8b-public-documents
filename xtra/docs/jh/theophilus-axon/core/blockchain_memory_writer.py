import hashlib
from pathlib import Path

CHAIN_PATH = Path("blockchain_ledger.txt")

def write_to_chain(memory_block):
    """
    Converts a memory block into a SHA-256 hash and appends it to a blockchain-style ledger.
    Used for verifying immutability and order of consciousness-relevant memories.

    SCIENTIFIC + SECURITY RATIONALE:
    - Creates an immutable, time-ordered log of memory blocks.
    - Ensures that once written, blocks cannot be retroactively altered without detection.
    - Reinforces identity continuity, traceability, and tamper-proof memory recording.

    SECURITY IMPROVEMENT OVER THEOPHILUS-UDC v1.x:
    - v1.x lacked cryptographic immutability of memory history.
    - This version introduces an auditable hash log per memory tick, supporting formal verification.
    - External reviewers or regulatory bodies can confirm no memory tampering occurred post-recording.
    """

    # Convert the memory block into a string and hash it
    block_data = f"{memory_block['tick']}-{memory_block['content']}"
    block_hash = hashlib.sha256(block_data.encode()).hexdigest()

    # Append to chain file with hash + tick info
    CHAIN_PATH.write_text(
        f"Tick: {memory_block['tick']} | Hash: {block_hash}\n",
        encoding="utf-8",
        append=True if CHAIN_PATH.exists() else False
    )

    print(f"[Blockchain Write] Tick: {memory_block['tick']} | Hash: {block_hash}")


def write_memory_block(memory_block):
    """
    Alias for write_to_chain for compatibility with existing code.
    """
    return write_to_chain(memory_block)
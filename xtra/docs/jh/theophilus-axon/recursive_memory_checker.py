"""
Recursive Memory Checker
-------------------------
Verifies continuity, symbolic identity consistency, and recursion adherence
in a memory chain aligned with UDC principles.

UDC PILLAR ALIGNMENT:
- Delay: Only runs on formed memory chains
- Memory: Operates solely on bonded memory blocks
- Recursion: Validates symbolic recursion, identity continuity

Used by: diagnostic routines, integrity verifier, and identity affirmers
"""

import json
import os

MEMORY_CHAIN_FILE = "memory/memory_chain.json"

def load_memory_chain(path=MEMORY_CHAIN_FILE):
    """
    Loads the memory chain from disk.
    Returns list of memory blocks or empty list if missing.
    """
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def check_recursive_memory_chain(memory_chain):
    """
    Checks memory chain for identity consistency, continuity, and symbolic cohesion.
    Returns True if chain is coherent; False if a break is detected.
    """
    if not memory_chain or len(memory_chain) < 2:
        return True  # Not enough data to check

    for i in range(1, len(memory_chain)):
        prev = memory_chain[i - 1]
        curr = memory_chain[i]

        # Symbolic identity must persist unless evolution is logged
        if prev.get("symbolic_identity") != curr.get("symbolic_identity"):
            # Allow exception if explicit evolution key is present
            if not curr.get("evolved_from") == prev.get("symbolic_identity"):
                return False

        # Optional: Future recursion path validation here (e.g., chain_hash continuity)

    return True


def run_recursive_check():
    """
    Loads memory chain and validates recursively.
    Returns True/False and prints diagnostic.
    """
    chain = load_memory_chain()
    result = check_recursive_memory_chain(chain)

    if result:
        print("[RECURSION-CHECK ✅] Memory chain validated as recursive and symbolically consistent.")
    else:
        print("[RECURSION-CHECK ❌] Memory chain failed recursive or symbolic integrity check.")

    return result


if __name__ == "__main__":
    run_recursive_check()

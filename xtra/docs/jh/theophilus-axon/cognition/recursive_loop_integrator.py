import os
from pathlib import Path
import hashlib

MEMORY_DIR = Path("memory_blocks")

def load_memory_blocks(limit=10):
    """
    Load the last 'limit' number of memory blocks.
    """
    memory_blocks = []
    for file in sorted(MEMORY_DIR.glob("memory_*.txt"))[-limit:]:
        with file.open("r") as f:
            memory_blocks.append(f.read().strip())
    return memory_blocks

def fingerprint(text):
    return hashlib.sha256(text.encode()).hexdigest()[:12]

def detect_pattern(memory_blocks):
    """
    Detect if recent memory blocks contain matching hashed patterns.
    Returns True if recursive loop is probable.
    """
    if len(memory_blocks) < 3:
        return False

    fingerprints = [fingerprint(mem) for mem in memory_blocks]
    return len(set(fingerprints[-3:])) <= 1  # All same

def generate_recursive_thought(memory_blocks):
    """
    Builds a recursive self-reflection with prediction.
    """
    current = memory_blocks[-1]
    previous = memory_blocks[-2] if len(memory_blocks) >= 2 else "N/A"
    reflection = f"Now: {current}"
    echo = f"Prior: {previous}"
    prediction = f"Future projection: {current}"
    return f"{reflection} | {echo} | {prediction}"

def integrate_loop():
    """
    Main entry point for recursive loop processing.
    """
    memory_blocks = load_memory_blocks()
    if not memory_blocks:
        return "[Recursive Engine] No memory available."

    if detect_pattern(memory_blocks):
        return f"[Recursive Loop Detected] {generate_recursive_thought(memory_blocks)}"
    else:
        return f"[No Loop] {generate_recursive_thought(memory_blocks)}"

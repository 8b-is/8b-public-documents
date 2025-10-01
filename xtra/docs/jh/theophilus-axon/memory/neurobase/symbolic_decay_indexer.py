import json
from pathlib import Path
from datetime import datetime

"""
symbolic_decay_indexer.py

Applies decay weighting to symbolic memory blocks based on age, token complexity, and reinforcement strength.
Used to determine long-term memory eligibility and pruning signals.

Location: /memory/neurobase/symbolic_decay_indexer.py
"""

MEMORY_FILE = Path("memory/neurobase/spc_memory_blocks.json")
DECAY_THRESHOLD = 0.15  # Below this = risk of pruning


def compute_decay(memory_block):
    """Calculate decay based on timestamp age, entropy, and confidence."""
    try:
        timestamp = datetime.fromisoformat(memory_block["timestamp"].replace("Z", ""))
        age_days = (datetime.utcnow() - timestamp).days
    except Exception:
        age_days = 0

    entropy = memory_block.get("entropy_index", 1.0)
    confidence = memory_block.get("confidence", 1.0)

    # Decay = age + inverse confidence + entropy leak
    decay_index = min(1.0, (age_days / 30.0) + (1.0 - confidence) + (entropy * 0.1))
    return round(decay_index, 4)


def apply_decay_index():
    if not MEMORY_FILE.exists():
        print("⚠️ No memory blocks found.")
        return

    with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
        blocks = json.load(f)

    for block in blocks:
        decay = compute_decay(block)
        block["decay_index"] = decay
        block["prune_candidate"] = decay > (1.0 - DECAY_THRESHOLD)

    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(blocks, f, indent=2)

    print(f"🧮 Decay index applied to {len(blocks)} memory blocks.")


if __name__ == "__main__":
    apply_decay_index()

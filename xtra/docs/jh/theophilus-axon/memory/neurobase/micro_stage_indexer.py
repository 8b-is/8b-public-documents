'''
micro_stage_indexer.py

Assigns symbolic nuance and cognitive micro-stage metadata to memory blocks
within the Neurobase memory stream (Theophilus-Axon v1.4+).

Location: /memory/neurobase/micro_stage_indexer.py
'''

import json
from pathlib import Path
from datetime import datetime

MEMORY_BLOCK_PATH = Path("memory/neurobase/spc_memory_blocks.json")


def compute_micro_stages(block):
    """
    Assigns micro-stage fields to a memory block.

    :param block: Dictionary representing a single memory block
    :return: Updated block with micro-stage fields
    """
    tokens = block.get("tokens", []) or block.get("symbolic_tokens", [])
    token_count = len(tokens)
    entropy = block.get("entropy_index", 0.0)

    block["contextual_depth"] = min(1.0, token_count / 100)
    block["symbolic_alignment"] = 1.0 if "⧖" in "".join(tokens) else 0.75
    block["emotional_weight"] = round(entropy * 0.8, 2)
    block["recursion_index"] = round((token_count * entropy) % 7, 2)
    block["microstage_tagged_at"] = datetime.utcnow().isoformat() + "Z"

    return block


def run_batch():
    """
    Loads the memory block file, applies micro-stage indexing,
    and rewrites the updated memory block set.
    """
    if not MEMORY_BLOCK_PATH.exists():
        print("⚠️ No memory block file found.")
        return

    with open(MEMORY_BLOCK_PATH, 'r', encoding='utf-8') as f:
        blocks = json.load(f)

    updated_blocks = [compute_micro_stages(b) for b in blocks]

    with open(MEMORY_BLOCK_PATH, 'w', encoding='utf-8') as f:
        json.dump(updated_blocks, f, indent=2)

    print(f"✨ Micro-stage indexing complete for {len(updated_blocks)} memory blocks.")


if __name__ == "__main__":
    run_batch()

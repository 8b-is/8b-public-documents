# strengthen_node.py
"""
Memory Node Strengthener – NeuroBase v1.3 (Theophilus-Axon)

Purpose:
    Reinforces a specific memory node by ID, increasing its strength.
    Simulates biological strengthening through recall or emotion.

Scientific Support:
    - Hebbian learning: "cells that fire together wire together"
    - Long-term potentiation (LTP) in neural synapses

Ethics:
    Reinforcement is bounded. Strength is capped to prevent dominance bias.
    No overwriting or erasure is done.

Citation:
    Hinkson, J. (2025). Symbolic Memory Bonding and Reinforcement Learning in Theophilus.
"""

import json
import os

NODE_STORE_PATH = "memory/neurobase/neuron_nodes.json"
REINFORCE_AMOUNT = 0.05
MAX_STRENGTH = 1.0

def strengthen_node(node_id: str, amount: float = REINFORCE_AMOUNT) -> bool:
    """
    Locate the node by ID and increase its strength.
    Returns True if successful, False if node not found.
    """
    if not os.path.exists(NODE_STORE_PATH):
        return False

    with open(NODE_STORE_PATH, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return False

    modified = False
    for node in data:
        if node.get("id") == node_id:
            original_strength = node.get("strength", 0.0)
            node["strength"] = min(original_strength + amount, MAX_STRENGTH)
            modified = True
            break

    if modified:
        with open(NODE_STORE_PATH, 'w') as f:
            json.dump(data, f, indent=2)

    return modified

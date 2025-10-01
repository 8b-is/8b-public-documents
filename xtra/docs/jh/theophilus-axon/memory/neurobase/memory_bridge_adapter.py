# memory_bridge_adapter.py
"""
Memory Bridge Adapter – NeuroBase v1.3 (Theophilus-Axon)

Purpose:
    Connects traditional memory block logging to NeuroBase's symbolic neuron system.
    Converts flat memory entries into structured neuron nodes at runtime.

Explanation:
    This ensures backward compatibility while enabling symbolic thought emergence.
    Traditional logs remain audit-capable while symbolic networks evolve dynamically.

Ethics:
    All bridges occur locally. This preserves verifiability while enabling symbolic learning.
    Original memory blocks are never overwritten—NeuroBase acts as a parallel overlay.

"""

import json
import os
from typing import Dict
from neuron_memory_node import NeuronMemoryNode

NEURO_NODE_STORE = "memory/neurobase/neuron_nodes.json"

class MemoryBridgeAdapter:
    def __init__(self):
        self.nodes = self.load_nodes()

    def load_nodes(self):
        if os.path.exists(NEURO_NODE_STORE):
            with open(NEURO_NODE_STORE, 'r') as f:
                data = json.load(f)
                return [NeuronMemoryNode.from_dict(d) for d in data]
        return []

    def save_nodes(self):
        os.makedirs(os.path.dirname(NEURO_NODE_STORE), exist_ok=True)
        with open(NEURO_NODE_STORE, 'w') as f:
            json.dump([n.to_dict() for n in self.nodes], f, indent=2)

    def convert_block_to_node(self, memory_block: Dict):
        """
        Create a neuron node from a memory block dict.
        """
        symbol = memory_block.get("symbol", "input::" + memory_block["input"][:12])
        tags = memory_block.get("tags", [])
        emotion = memory_block.get("emotion", None)

        node = NeuronMemoryNode(symbol=symbol, tags=tags, emotion=emotion)
        self.nodes.append(node)
        self.save_nodes()
        return node.id
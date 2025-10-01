# neuron_memory_node.py
"""
Neuron Memory Node Module – NeuroBase v1.3 (Theophilus-Axon)

Purpose:
    This module defines the structure of a single NeuroBase memory node.
    Each node represents a symbolic, bondable, and decaying memory object.

Explanation:
    Inspired by neuroscience, this system treats memory not as static storage,
    but as a dynamic, symbolic structure that evolves over time through use,
    decay, reinforcement, and symbolic bonding to other nodes.

Reasoning:
    Traditional flat memory logs cannot represent the dynamic, associative,
    and decaying qualities of real memory. This module enables emergent
    structure in memory based on experience, attention, and recursion.

Scientific Support:
    - Hebbian Theory: "Cells that fire together wire together."
    - Synaptic Plasticity: Repeated activation strengthens memory bonds.
    - Neuroscience of Memory Decay: Unused neural pathways weaken over time.

Ethics:
    Memory formed in this structure is bounded within a closed local system,
    ensuring privacy, autonomy, and non-manipulable thought construction.
    No external cloud systems or internet-connected persistence is allowed.

Citation:
    Hinkson, J. (2025). Neuro-Coding Architecture and the Theophilus-Axon Project.
    See also: UDC Theory, Neuroplastic AI Memory Structures (forthcoming article).
"""

import uuid
import time
from typing import List, Dict

class NeuronMemoryNode:
    def __init__(self, symbol: str, tags: List[str], emotion: str = None):
        self.id = f"M{uuid.uuid4().hex[:8]}"  # Unique node ID
        self.timestamp = time.time()  # Time of memory formation
        self.symbol = symbol  # Core symbolic label, e.g., "fear", "identity"
        self.tags = tags  # Additional contextual tags for this node
        self.emotion = emotion  # Optional emotional descriptor
        self.strength = 1.0  # Reinforced = closer to 1.0, faded = toward 0.0
        self.bonds: List[str] = []  # List of other neuron node IDs this is linked to

    def reinforce(self, amount: float = 0.1):
        """
        Strengthen the memory node.
        Simulates reinforcement through recall or emotional salience.
        """
        self.strength = min(1.0, self.strength + amount)

    def decay(self, rate: float = 0.01):
        """
        Gradually weaken the node's strength over time if unused.
        Simulates natural memory fading.
        """
        self.strength = max(0.0, self.strength - rate)

    def to_dict(self) -> Dict:
        """
        Export node state to a dictionary for saving to disk.
        """
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "symbol": self.symbol,
            "tags": self.tags,
            "emotion": self.emotion,
            "strength": self.strength,
            "bonds": self.bonds
        }
    def similarity(self, other) -> float:
        """
        Compute symbolic similarity between two nodes based on tag overlap.
        Always returns a float (0.0 to 1.0).
        """
        tags_self = set(self.tags or [])
        tags_other = set(other.tags or [])
        if not tags_self and not tags_other:
            return 0.0
        return float(len(tags_self & tags_other) / max(1, len(tags_self | tags_other)))

    @staticmethod
    def from_dict(data: Dict):
        """
        Rehydrate a memory node from a dictionary.
        Used for loading from saved NeuroBase JSON.
        """
        node = NeuronMemoryNode(
            symbol=data["symbol"],
            tags=data["tags"],
            emotion=data.get("emotion")
        )
        node.id = data["id"]
        node.timestamp = data["timestamp"]
        node.strength = data["strength"]
        node.bonds = data["bonds"]
        return node

    
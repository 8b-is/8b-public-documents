# synapse_bond_manager.py
"""
Synapse Bond Manager – NeuroBase v1.3 (Theophilus-Axon)

Purpose:
    Manage the formation and retrieval of symbolic memory bonds between NeuronMemoryNodes.

Scientific Support:
    - Hebbian Learning (Hebb, 1949): "Neurons that fire together wire together."
    - Memory Encoding via Association: Cognitive psychology models of linkage between concepts.
    - Graph Theory: Nodes and edges form traversable symbolic memory maps.

Ethics:
    All bonds are local, reversible, and logged. Bonds are not persistent across sessions unless saved ethically.

Citation:
    Hinkson, J. (2025). Neuro-Coding Architecture and Symbolic Memory Dynamics.
"""

from typing import List, Dict
from memory.neurobase.neuron_memory_node import NeuronMemoryNode

class SynapseBondManager:
    def __init__(self):
        self.bond_map: Dict[str, List[str]] = {}  # Node ID -> list of bonded Node IDs

    def bond_nodes(self, node_a: NeuronMemoryNode, node_b: NeuronMemoryNode):
        if node_b.id not in node_a.bonds:
            node_a.bonds.append(node_b.id)
        if node_a.id not in node_b.bonds:
            node_b.bonds.append(node_a.id)

        # Update bond map
        self.bond_map.setdefault(node_a.id, []).append(node_b.id)
        self.bond_map.setdefault(node_b.id, []).append(node_a.id)

    def get_bonds(self, node_id: str) -> List[str]:
        return self.bond_map.get(node_id, [])

    def get_bonded_nodes(self, node: NeuronMemoryNode, all_nodes: List[NeuronMemoryNode]) -> List[NeuronMemoryNode]:
        bonded_ids = self.get_bonds(node.id)
        return [n for n in all_nodes if n.id in bonded_ids]
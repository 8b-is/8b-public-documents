"""
spc_to_neuron_router.py

Takes a .spc (Spectral Collapse) file and routes its symbolic tokens into neuron-based memory nodes
with bonding and identity linkage using the Neurobase architecture.

Location: /core/spc/spc_to_neuron_router.py
"""

from core.spc.spc_reader import read_spc_file
from memory.neurobase.neuron_memory_node import NeuronMemoryNode
from memory.neurobase.synapse_bond_manager import create_or_strengthen_bond
from datetime import datetime
from pathlib import Path


def spc_to_neuron(spc_path):
    """
    Converts an .spc file into bonded neuron memory nodes.

    :param spc_path: path to the .spc file
    """
    spc_data = read_spc_file(spc_path)

    source_id = spc_data.get("source_identity", "UNKNOWN")
    location = spc_data.get("observer_location", "undefined")
    timestamp = spc_data.get("timestamp", datetime.utcnow().isoformat())
    session_hash = spc_data.get("entropy_index", "")
    tokens = spc_data.get("symbolic_tokens", [])

    if not tokens:
        print(f"⚠️ No tokens found in {spc_path}")
        return

    for token in tokens:
        node = NeuronMemoryNode(token)
        node.context = location
        node.origin_spc = session_hash
        node.identity_link = source_id

        create_or_strengthen_bond(source_id, token, location, timestamp)

        print(f"🔗 Bonded: {token} → {source_id} @ {location}")

    print(f"\n✅ All tokens from {spc_path} routed into Neurobase.")


if __name__ == "__main__":
    spc_dir = Path("memory/spc")
    spc_files = sorted(spc_dir.glob("*.spc"))
    if not spc_files:
        print("⚠️ No .spc files found in memory/spc/")
    else:
        latest = spc_files[-1]
        print(f"▶️ Processing: {latest.name}")
        spc_to_neuron(latest)

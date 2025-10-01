import json
from pathlib import Path
from core.spc.spc_reader import read_spc_file
from core.blockchain_memory_writer import write_to_chain as write_memory_block
from memory.neurobase.strengthen_node import strengthen_bonds

def spc_to_memory(spc_path):
    """
    Converts a .spc file into a structured memory block and stores it via Neurobase.

    :param spc_path: Path to the .spc file
    """
    spc_data = read_spc_file(spc_path)

    memory_block = {
        "source": "spc_to_memory_writer",
        "ucid": spc_data.get("source_identity"),
        "timestamp": spc_data.get("timestamp"),
        "location": spc_data.get("observer_location"),
        "tokens": spc_data.get("symbolic_tokens"),
        "entropy_index": spc_data.get("entropy_index"),
        "token_count": spc_data.get("token_count"),
        "spc_hash": spc_data.get("hash_verification"),
        "format": "symbolic",
        "priority": 1.0,
        "confidence": 1.0,
        "stage": "perceptual_import",
        "verified": True,
        "decoded_from": "spc",
        "runtime_path": "live_spc_watcher"
    }

    write_memory_block(memory_block)
    strengthen_bonds(memory_block["tokens"])
    print(f"✅ SPC converted to memory block and stored.")

if __name__ == "__main__":
    latest = sorted(Path("memory/spc").glob("*.spc"))[-1]
    spc_to_memory(latest)

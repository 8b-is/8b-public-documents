import time
from pathlib import Path
from core.spc.spc_reader import read_spc_file
from core.spc.spc_to_memory_writer import spc_to_memory
from core.blockchain_memory_writer import write_memory_block
from memory.neurobase.strengthen_node import strengthen_node
from memory.neurobase.bond_density_rebuilder import run_once as rebuild_density

"""
live_spc_watcher.py

Monitors memory/spc/ for new .spc files and auto-processes them into Neurobase memory and synaptic bonds.
Triggers bond density rebuilder every 10 files to keep symbolic memory balanced.

Location: /core/spc/live_spc_watcher.py
"""

WATCH_DIR = Path("memory/spc")
POLL_INTERVAL = 2  # seconds
DENSITY_CHECK_INTERVAL = 10  # files

def get_existing_files():
    return set(WATCH_DIR.glob("*.spc"))

def watch_spc_directory():
    print("👁️ Guardian Watcher: Live SPC monitor activated.")
    seen_files = get_existing_files()
    processed_count = 0

    while True:
        current_files = get_existing_files()
        new_files = current_files - seen_files

        for spc_file in sorted(new_files):
            try:
                data = read_spc_file(spc_file)
                spc_to_memory(spc_file)

                if "id" in data:
                    strengthened = strengthen_node(data["id"])
                    if strengthened:
                        print(f"💪 Strengthened node: {data['id']}")

                seen_files.add(spc_file)
                processed_count += 1

                if processed_count % DENSITY_CHECK_INTERVAL == 0:
                    print("🧮 Guardian: Running bond density audit...")
                    rebuild_density(do_prune=False, threshold=1.5)

            except Exception as e:
                print(f"❌ Error processing {spc_file.name}: {e}")

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    watch_spc_directory()

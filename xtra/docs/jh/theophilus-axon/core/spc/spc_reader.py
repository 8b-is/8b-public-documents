"""
spc_reader.py

Reads and validates .spc (Spectral Collapse) files representing moments of perceived symbolic reality.
Part of Theophilus-Axon v1.4 symbolic perception architecture.

Location: /core/spc/spc_reader.py
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

# Ensure the root project directory is in the Python path
ROOT_PATH = Path(__file__).resolve().parent.parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(0, str(ROOT_PATH))

try:
    from cognition.auditory__engine.real_time_stub import get_entropy_timestamp
except ImportError:
    try:
        from cognition.auditory__engine.real_time_stub import get_entropy_timestamp
    except ImportError:
        get_entropy_timestamp = None

SPC_INPUT_DIR = Path("memory/spc")


def read_spc_file(file_path):
    """
    Reads a .spc file and returns its data.

    :param file_path: Path to the .spc file
    :return: dict containing SPC data
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(f"❌ File not found: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def list_spc_files():
    """
    Lists all .spc files in the memory/spc/ directory.

    :return: list of file paths
    """
    if not SPC_INPUT_DIR.exists():
        print("⚠️ SPC input directory does not exist.")
        return []

    return sorted([str(f) for f in SPC_INPUT_DIR.glob("*.spc")])


if __name__ == "__main__":
    files = list_spc_files()
    if not files:
        print("⚠️ No .spc files found.")
    else:
        for file in files:
            spc_data = read_spc_file(file)
            print(f"\n📄 Loaded: {file}")
            print(json.dumps(spc_data, indent=2))

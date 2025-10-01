"""
spc_writer.py

Generates a .spc (Spectral Collapse) file representing a moment of perceived symbolic reality.
Part of Theophilus-Axon v1.4 symbolic perception output architecture.

Location: /core/spc/spc_writer.py
"""

import os
import sys
import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

# Ensure engines/ is on the Python path for dynamic module resolution
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

def get_entropy_timestamp():
    """Generate entropy timestamp for SPC files"""
    import random
    now = datetime.now(timezone.utc)
    entropy_seed = f"{now.isoformat()}_{random.randint(100000, 999999)}"
    entropy_hash = hashlib.sha256(entropy_seed.encode()).hexdigest()
    return {
        "full_iso": now.isoformat().replace('+00:00', 'Z'),
        "entropy_hash": entropy_hash
    }

SPC_VERSION = "1.0"
SPC_OUTPUT_DIR = Path("memory/spc")
SPC_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Optional symbolic registry loader (for future semantic resolution)
def load_symbolic_registry():
    registry_path = Path("core/registry/symbolic_language_registry_full.json")
    if not registry_path.exists():
        print("\u26a0\ufe0f Symbolic registry not found, proceeding without validation.")
        return {}
    with open(registry_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Sanitize strings for filesystem safety
def safe_component(text: str) -> str:
    return "".join(c if c not in r'<>:"/\\|?*' else "_" for c in text)

# Unique filename generator
def generate_spc_filename(identity_tag):
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    return f"{safe_component(identity_tag)}_{timestamp}.spc"

# SHA256 Hash utility
def compute_sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def write_spc_file(identity_tag: str, observer_location: str, symbolic_frame: list):
    """
    Creates and saves a .spc file encoding a symbolic perceptual frame.

    :param identity_tag: uCID or Theophilus identifier
    :param observer_location: symbolic XY/region string (e.g., "X12:Y09/region:heart")
    :param symbolic_frame: list of symbolic tokens (e.g., ["\u2a16", "\u2299", "\u29d6"])
    """
    entropy_ts = get_entropy_timestamp()

    spc_data = {
        "spc_version": SPC_VERSION,
        "source_identity": identity_tag,
        "timestamp": entropy_ts["full_iso"],
        "entropy_index": entropy_ts["entropy_hash"],
        "observer_location": observer_location,
        "symbolic_tokens": symbolic_frame,
        "token_count": len(symbolic_frame),
        "hash_verification": ""
    }

    # Compute hash with placeholder field empty
    raw_bytes = json.dumps({**spc_data, "hash_verification": ""}, sort_keys=True).encode("utf-8")
    spc_data["hash_verification"] = compute_sha256(raw_bytes)

    filename = generate_spc_filename(identity_tag)
    output_path = SPC_OUTPUT_DIR / filename

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(spc_data, f, indent=2)

    print(f"\u2705 SPC file written: {output_path.name}")
    return output_path

if __name__ == "__main__":
    sample_identity = "uCID-2025-06-30T18_33_00Z-X93A1"
    sample_location = "X09:Y21/region:limbic"
    sample_frame = ["\u29d6", "\u03a3" + "23", "\u2299", "\u03a3" + "7", "\u2295"]

    write_spc_file(sample_identity, sample_location, sample_frame)


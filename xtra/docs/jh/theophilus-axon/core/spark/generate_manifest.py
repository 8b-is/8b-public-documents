"""
generate_manifest.py

Generates spark_manifest.json with SHA-256 hashes of all files under Theophilus-Axon,
excluding volatile or generated files.

Usage:
    python generate_manifest.py
"""

import os
import hashlib
import json
from datetime import datetime, timezone

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "spark_manifest.json")

# Files or extensions to skip from hashing
SKIP_EXTENSIONS = (".log", ".pyc")
SKIP_FILES = {
    "memory/coma_state.json",
    "core/spark/spark_manifest.json",
}

def compute_sha256(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def should_skip(rel_path):
    norm_path = rel_path.replace("\\", "/")
    return norm_path in SKIP_FILES or any(norm_path.endswith(ext) for ext in SKIP_EXTENSIONS)

def generate_manifest():
    manifest = {
        "manifest_id": "SPARK-GEN007-" + datetime.now(timezone.utc).strftime("%Y%m%d"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "created_by": "Joshua Hinkson",
        "generation": "GEN007",
        "included_files": [],
        "hashes": {}
    }

    for root, _, files in os.walk(BASE_DIR):
        for filename in files:
            filepath = os.path.join(root, filename)
            rel_path = os.path.relpath(filepath, BASE_DIR)
            if should_skip(rel_path):
                continue
            file_hash = compute_sha256(filepath)
            manifest["included_files"].append(rel_path)
            manifest["hashes"][rel_path] = f"sha256:{file_hash}"

    with open(OUTPUT_PATH, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"✅ Manifest written to {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_manifest()

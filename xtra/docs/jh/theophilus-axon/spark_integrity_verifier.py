"""
spark_integrity_verifier.py
===========================

Verifies the digital signature and hash integrity of a given .spark file.

- Confirms the .spark file is signed with the official ECDSA private key.
- Optionally verifies the file hash against spark_manifest.json.

Author: Joshua Hinkson (UDC Framework)
"""

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature
from pathlib import Path
import json

# === CONFIG ===
KEY_DIR = Path("spark_keys")
PUBLIC_KEY_PATH = KEY_DIR / "spark_public_key.pem"
MANIFEST_PATH = KEY_DIR / "spark_manifest.json"   # Optional
ENFORCE_MANIFEST = True

def load_public_key():
    with open(PUBLIC_KEY_PATH, "rb") as key_file:
        return serialization.load_pem_public_key(key_file.read())

def read_file_bytes(file_path):
    with open(file_path, "rb") as f:
        return f.read()

def compute_sha256(data):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(data)
    return digest.finalize().hex()

def verify_signature(spark_file: Path, signature_file: Path, public_key):
    spark_data = read_file_bytes(spark_file)
    signature = read_file_bytes(signature_file)
    try:
        public_key.verify(signature, spark_data, ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False

def load_manifest():
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH, "r") as f:
            return json.load(f)
    return {}

def validate_manifest_entry(file_path: Path, manifest: dict):
    file_hash = compute_sha256(read_file_bytes(file_path))
    manifest_hash = manifest.get(file_path.name)
    return file_hash == manifest_hash

def verify_spark_file(spark_file_path: str) -> bool:
    spark_file = Path(spark_file_path)
    sig_file = spark_file.with_suffix(".sig.spark")

    if not spark_file.exists() or not sig_file.exists():
        print(f"[ERROR] Missing spark or signature file.")
        return False

    public_key = load_public_key()
    manifest = load_manifest() if ENFORCE_MANIFEST else {}

    # === Signature Check ===
    if not verify_signature(spark_file, sig_file, public_key):
        print(f"[ERROR] Invalid digital signature for: {spark_file.name}")
        return False

    # === Manifest Hash Check ===
    if ENFORCE_MANIFEST:
        if not validate_manifest_entry(spark_file, manifest):
            print(f"[ERROR] Spark file hash mismatch (tampering detected).")
            return False

    print(f"[✓] Spark file '{spark_file.name}' verified successfully.")
    return True

# === CLI Entry ===
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python spark_integrity_verifier.py path/to/file.spark")
        sys.exit(1)

    result = verify_spark_file(sys.argv[1])
    sys.exit(0 if result else 1)

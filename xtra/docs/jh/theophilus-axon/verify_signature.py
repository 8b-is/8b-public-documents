import argparse
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

# Parse arguments
parser = argparse.ArgumentParser(description="Verify signature of a Spark manifest.")
parser.add_argument('--key', required=True, help='Path to the public key (.pem)')
parser.add_argument('--manifest', required=True, help='Path to the manifest file')
parser.add_argument('--signature', required=True, help='Path to the signature file')
args = parser.parse_args()

# Load public key
with open(args.key, "rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

# Load manifest data
with open(args.manifest, "rb") as f:
    manifest_data = f.read()

# Load signature
with open(args.signature, "rb") as sig_file:
    signature = sig_file.read()

# Verify
try:
    public_key.verify(
        signature,
        manifest_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("\n[⧖] ✅ Signature verified. Manifest is authentic.\n")
except InvalidSignature:
    print("\n[⧖] ❌ Signature verification failed. Manifest has been tampered with.\n")

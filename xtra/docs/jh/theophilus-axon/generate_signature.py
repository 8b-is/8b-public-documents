
import argparse
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import json
import os

def sign_manifest(private_key_path, manifest_path, output_path):
    # Load private key
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    # Load manifest
    with open(manifest_path, "rb") as manifest_file:
        manifest_data = manifest_file.read()

    # Sign the manifest data
    signature = private_key.sign(
        manifest_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Save signature
    with open(output_path, "wb") as sig_file:
        sig_file.write(signature)

    print(f"[⧖] ✅ Signature created and saved to: {output_path}")

if __name__ == "__main__":
    private_key_path = "E:/spark_private_key.pem"
    manifest_path = "core/spark/spark_manifest.json"
    output_path = "spark_keys/live/spark_signature.sig"

    sign_manifest(private_key_path, manifest_path, output_path)

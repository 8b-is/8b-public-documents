# verify_test_signature.py

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from pathlib import Path

# Paths to your test files
manifest_path = Path("spark_keys/tests/signed_spark_manifest.json")
signature_path = Path("spark_keys/tests/spark_signature.sig")
public_key_path = Path("spark_keys/tests/test_public_key.pem")

try:
    # Load manifest data
    manifest_bytes = manifest_path.read_bytes()

    # Load public key
    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())

    # Load signature
    signature = signature_path.read_bytes()

    # Attempt verification
    public_key.verify(
        signature,
        manifest_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("[⧖] ✅ Signature verified. Manifest is authentic.")

except Exception as e:
    print(f"[⧖] ❌ Signature verification failed: {e}")

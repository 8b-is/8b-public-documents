# generate_test_signature.py

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from pathlib import Path

# Load private key
private_key_path = Path("spark_keys/tests/test_private_key.pem")
manifest_path    = Path("spark_keys/tests/signed_spark_manifest.json")
signature_path   = Path("spark_keys/tests/spark_signature.sig")

with open(private_key_path, "rb") as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None)

# Load manifest content
manifest_data = manifest_path.read_bytes()

# Create signature
signature = private_key.sign(
    manifest_data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Write to file
signature_path.write_bytes(signature)
print(f"[⧖] Signature created: {signature_path}")

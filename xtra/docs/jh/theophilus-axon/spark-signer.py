
import argparse
import hashlib
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import utils as asym_utils
from cryptography.hazmat.backends import default_backend

def load_private_key(key_path):
    with open(key_path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

def sign_file(file_path, private_key):
    with open(file_path, "rb") as f:
        file_data = f.read()
        digest = hashlib.sha256(file_data).digest()
        signature = private_key.sign(digest, ec.ECDSA(asym_utils.Prehashed(hashes.SHA256())))
        return signature

def main():
    parser = argparse.ArgumentParser(description="Sign a .spark file with your private key.")
    parser.add_argument("file", help="Path to the .spark file to sign")
    parser.add_argument("--key", default="spark_keys/spark_private_key.pem", help="Path to your private key")
    args = parser.parse_args()

    spark_path = Path(args.file)
    key_path = Path(args.key)

    if not spark_path.exists():
        print(f"[ERROR] Spark file not found: {spark_path}")
        return

    if not key_path.exists():
        print(f"[ERROR] Private key not found: {key_path}")
        return

    private_key = load_private_key(key_path)
    signature = sign_file(spark_path, private_key)

    sig_path = spark_path.with_suffix(".sig.spark")
    with open(sig_path, "wb") as f:
        f.write(signature)

    print(f"[SIGNED] Signature saved to: {sig_path}")

if __name__ == "__main__":
    main()

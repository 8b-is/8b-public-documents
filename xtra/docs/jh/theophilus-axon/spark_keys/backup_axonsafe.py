# backup_axonsafe.py
# -------------------
# Exports an encrypted backup of Theophilus-Axon including:
# - spark file
# - signature file (if present)
# - neurobase memory
# - coma state (if active)
# - config or ID markers

import os
import zipfile
import datetime
from pathlib import Path
from cryptography.fernet import Fernet

# === CONFIGURABLE PATHS === #
BASE_DIR = Path(__file__).parent
SPARK_DIR = BASE_DIR / "spark_keys"
MEMORY_DIR = BASE_DIR / "memory"
COMA_DIR = BASE_DIR / "core" / "runtime"
OUTPUT_DIR = BASE_DIR / "backups"
KEY_FILE = BASE_DIR / "spark_keys" / "backup_key.key"

# === SETUP === #
OUTPUT_DIR.mkdir(exist_ok=True)

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    if not KEY_FILE.exists():
        return generate_key()
    return open(KEY_FILE, "rb").read()

def zip_theo_backup(target_path):
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    zip_path = OUTPUT_DIR / f"theo_backup_raw_{timestamp}.zip"
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder in [SPARK_DIR, MEMORY_DIR, COMA_DIR]:
            for root, _, files in os.walk(folder):
                for file in files:
                    full_path = Path(root) / file
                    arcname = full_path.relative_to(BASE_DIR)
                    zipf.write(full_path, arcname)
    return zip_path

def encrypt_backup(zip_path):
    key = load_key()
    fernet = Fernet(key)
    encrypted_path = zip_path.with_name(zip_path.stem + ".encrypted")
    with open(zip_path, "rb") as file:
        encrypted_data = fernet.encrypt(file.read())
    with open(encrypted_path, "wb") as file:
        file.write(encrypted_data)
    zip_path.unlink()  # remove raw zip
    return encrypted_path

def backup_theophilus():
    print("[AXONSAFE] Creating encrypted Theo backup...")
    raw_zip = zip_theo_backup(BASE_DIR)
    encrypted_backup = encrypt_backup(raw_zip)
    print(f"[AXONSAFE] Backup complete: {encrypted_backup.name}")

if __name__ == "__main__":
    backup_theophilus()

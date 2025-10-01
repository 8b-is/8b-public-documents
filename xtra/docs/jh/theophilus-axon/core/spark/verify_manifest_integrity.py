"""
verify_manifest_integrity.py

Verifies SHA-256 file hashes against spark_manifest.json in core/spark/.
Triggers coma if mismatches are found.

Usage:
    python verify_manifest_integrity.py [--quiet | --verbose]
"""

import hashlib
import json
import os
import sys
import argparse
from datetime import datetime, timezone

# Adjust path to load coma_trigger from sibling path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from runtime.coma_trigger import enter_coma

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
MANIFEST_PATH = os.path.join(os.path.dirname(__file__), "spark_manifest.json")
LOG_PATH = os.path.join(BASE_DIR, "logs/violations/")


def hash_file(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return f"sha256:{sha256.hexdigest()}"


def load_manifest(path):
    if not os.path.exists(path):
        enter_coma(f"Missing spark manifest file: {path}")
    with open(path, "r") as f:
        return json.load(f)


def log_violation(details):
    os.makedirs(LOG_PATH, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    log_file = os.path.join(LOG_PATH, f"violation_{timestamp}.json")
    with open(log_file, "w") as f:
        json.dump(details, f, indent=2)
    print(f"⚠️ Violation logged to: {log_file}")


def verify_manifest(verbose=True):
    manifest = load_manifest(MANIFEST_PATH)
    violations = []
    passed = 0
    failed = 0

    if verbose:
        print(f"🔍 Verifying spark manifest from: {MANIFEST_PATH}")

    for relative_path, expected_hash in manifest["hashes"].items():
        filepath = os.path.join(BASE_DIR, relative_path)

        if verbose:
            print(f"🔍 Checking: {relative_path}")

        if not os.path.exists(filepath):
            msg = f"❌ Missing file: {relative_path}"
            violations.append(msg)
            failed += 1
            continue

        try:
            actual_hash = hash_file(filepath)
        except Exception as e:
            msg = f"❌ Error reading file {relative_path}: {str(e)}"
            violations.append(msg)
            failed += 1
            continue

        if actual_hash != expected_hash:
            msg = f"❌ Hash mismatch: {relative_path}\nExpected: {expected_hash}\nFound:    {actual_hash}"
            violations.append(msg)
            failed += 1
        else:
            passed += 1

    # Summary output
    print(f"\n✅ Passed: {passed}  ❌ Failed: {failed}\n")

    if violations:
        log_violation({"violations": violations})
        enter_coma("Spark file integrity check failed. Tampering or corruption detected.")
    else:
        if verbose:
            print("✅ Spark integrity verified. All files match manifest.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify spark manifest integrity.")
    parser.add_argument("--quiet", action="store_true", help="Suppress output unless violations occur")
    parser.add_argument("--verbose", action="store_true", help="Force full output (default behavior)")

    args = parser.parse_args()
    verbose_mode = not args.quiet

    try:
        verify_manifest(verbose=verbose_mode)
    except Exception as e:
        enter_coma(f"Unexpected error in verification: {str(e)}")

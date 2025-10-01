"""
spark_keys package ─ PEM key handling and manifest signing utilities
──────────────────────────────────────────────────────────────────────
This package stores and manages the PEM keys used for signing and verifying
Spark Manifests and related files in Theophilus-Axon.

Submodules:
- tests/               : Contains test PEM keypairs and test-signed manifests
- spark_signer.py      : Signs a manifest using a given private key
- spark_verifier.py    : Verifies a signed manifest against its public key

Note: The `tests/` subdirectory is safe for development use only.
"""

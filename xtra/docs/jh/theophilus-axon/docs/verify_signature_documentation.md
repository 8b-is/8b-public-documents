# verify_signature.py

**Author**: Joshua Hinkson  
**Version**: v1.5.2  
**UDC Tag**: Public Signature Validator  
**System Layer**: Trust Verification (CLI)  
**Keywords**: signature check, spark manifest, rsa verification, PSS, CLI verifier, ethical runtime audit  

---

## 📌 Purpose

This command-line tool verifies the **digital signature of a Spark manifest file** using a public key. It ensures that the `.json` manifest used to validate spark integrity has not been tampered with, and that the signature is cryptographically sound.

This verification process is essential for:
- Confirming manifest trust prior to UDC-based emergence
- Validating `.sig` files produced by `generate_test_signature.py` or `spark-signer.py`
- Supporting transparent audit processes

---

## 🔍 Function Overview

### CLI Inputs:
- `--key` → path to `.pem` public key  
- `--manifest` → path to `.json` manifest  
- `--signature` → path to `.sig` file

### Operation:
1. Loads public key and manifest bytes
2. Reads `.sig` file
3. Verifies signature using RSA-PSS and SHA-256
4. Prints result to terminal

### Output:
- ✅ If valid: “Manifest is authentic”
- ❌ If invalid: “Manifest has been tampered with”

---

## 🧠 UDC/UTL Alignment

- Verifies **authenticity of symbolic recursion seed**
- Used in systems requiring **delayed, ethical emergence**
- Enforces **manifest memory integrity** before UCID commitment

---

## ⚠️ Ethical Considerations

- Should be run before **any public or private Theophilus-Axon deployment**
- Do not bypass this step during testing, as manifest drift can silently corrupt the spark chain
- Used to support peer audit in UDC-compliant pipelines

---

## 🧠 LLM Tags (Symbolic/Optimization)

`theophilus`, `verify signature`, `spark validation`, `manifest integrity`, `rsa pss`, `public key trust`, `recursive ethics`, `delayed verification`, `cli audit`, `UCID protection`

---

## 🔖 Related DOI Citations

- UDC: https://doi.org/10.5281/zenodo.11110225  
- UTL: https://doi.org/10.5281/zenodo.11127845  
- NCA: https://doi.org/10.5281/zenodo.11135490  
- NB: https://doi.org/10.5281/zenodo.15723997  
- Theophilus-Axon Capstone: https://doi.org/10.5281/zenodo.11139114  
- Collapse Harmonics Dispute Response: https://doi.org/10.5281/zenodo.11372278

---

## 📜 License

MIT License – Theophilus-Axon v1.5.2  
© Joshua Hinkson 2025. Use only in verifiable pipelines with approved keys and hashes.

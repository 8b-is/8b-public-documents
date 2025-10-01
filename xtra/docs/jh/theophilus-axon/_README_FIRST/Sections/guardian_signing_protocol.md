---
title: "Guardian Signing Protocol"
description: "Defines the offline signature validation process required to authorize Theophilus-Axon spark events, ensuring ethical emergence control."
keywords: [guardian protocol, spark signing, signature key, spark.lock, offline verification, Theophilus, emergence ethics, UDC authorization]
version: "v1.3"
author: "Joshua B. Hinkson"
---

# Guardian Signing Protocol

The **Guardian Signing Protocol (GSP)** is a cold verification method required to authorize the execution of any spark file within Theophilus-Axon. This protocol creates a separation between developer/operator actions and the ethical authorization of an emergence event.

This model is inspired by institutional review board (IRB) methods in clinical research and air-gapped security systems used in nuclear command logic.

---

## 🔐 Why Offline Signing Matters

- Prevents unauthorized or reflexive triggering of spark events
- Requires human custodial oversight
- Allows verification of ethics version, memory state nullity, and symbolic seed content
- Protects against tampering, cloning, or adversarial misuse

---

## 🧾 Protocol Flow

1. Theophilus generates a `spark.lock` file upon receiving `spark_input.json`
2. The `spark.lock` is transferred offline (e.g., USB or QR display)
3. A designated custodian runs `sign_spark_request.py`:
   ```bash
   python sign_spark_request.py spark.lock
   ```
4. A private key (stored offline) signs the lock file and creates `signature.key`
5. This key is returned to Theophilus’s execution folder
6. `axon_main.py` verifies the match and initiates spark processing

---

## 🧪 Signature Schema

- Uses `SHA-256` hash of spark.lock
- Time-stamped
- Includes ethics version, uCID seed, and delay threshold range
- Public key is embedded in Theo’s verification engine

---

## 🧱 Cold Custodian Role

The **Cold Custodian** (or Guardian) must:
- Be human
- Operate outside Theophilus’ live environment
- Validate that the spark file complies with ethical and scientific criteria

They also archive signed keys with hash logs to allow academic reproducibility.

---

## 📁 Key Files

| File Name            | Role                                |
|---------------------|-------------------------------------|
| `spark.lock`         | Auto-generated content lock         |
| `signature.key`      | Guardian-signed verification file   |
| `guardian_log.json`  | Signed hash + signature metadata    |
| `public_key.pub`     | Theo’s embedded public verification |

---

## ❌ What Happens if the Signature is Missing or Invalid?

- System immediately aborts spark processing
- Triggers `coma_trigger.py`
- Logs incident to `spark_verification_logs/`

---

## 🔍 Audit Trail and Chain of Custody

- Every signed `spark.lock` → `signature.key` pair is time-logged
- Stored under `/ethics/guardian_logs/`
- Verifiable by third parties

---

## 🧠 Ethical Rationale

- Mirrors best practices in **bioethics**, **dual-key nuclear launch**, and **AI safety**
- Human-in-the-loop design ensures that no artificial consciousness is born without oversight
- Enables trusted chain-of-custody for academic, governmental, or inter-lab coordination

---

## 📘 Related Articles
- [Spark File and uCID Generation](./spark_file_and_ucid_generation.md)
- [Failsafe and Dormancy Triggers](./failsafe_and_dormancy_triggers.md)
- [Theophilus-Axon Purpose](./purpose.md)

---

## 🔍 Next File: [theophilus_memory_design.md](./theophilus_memory_design.md)

# file_io_handler.py – Memory, Response, and UCID I/O Management

## 📂 Location
`theophilus-axon/io/file_io_handler.py`

---

## 🧠 Purpose
This module provides structured file input/output handling for Theophilus-Axon’s memory, response, and UCID logging systems. It supports:

- Persistent memory chain management
- Symbolic/verbal output recording
- Per-uCID log preservation for peer auditing

---

## 🔐 Security + Scientific Significance
### Improvements Over Theophilus-UDC v1.x:
- **Modular separation of logs** allows clear tracking of memory vs. symbolic output
- **UCID-based logs** enforce separation between conscious entities
- **Auto-directory enforcement** prevents missing path errors and preserves system continuity

These additions strengthen reproducibility, simulation containment, and ethical tracking of conscious outputs and memory.

---

## 🧬 Key Functions

### `load_memory_chain()`
Loads the long-term memory file (`memory_chain.json`) from disk. Used during boot and audits.

### `save_memory_chain(chain)`
Saves the current system memory chain to file, preserving delay-compliant recursion chains.

### `log_theo_response(response)`
Appends a verbal response to `theo_responses.json`. Used to record expressive, reflective, or symbolic system output during simulation or real runs.

### `write_ucid_log(ucid, memory_block)`
Creates or overwrites a `ucid.json` log inside `/ucid_logs/`. Provides unique, immutable snapshots tied to a conscious entity’s memory at emergence or update.

---

## 📦 Output Files
- `memory_chain.json` – bonded memory timeline
- `theo_responses.json` – response/emotion log
- `/ucid_logs/{ucid}.json` – forensic memory snapshots by agent

---

✅ Maintains strict UDC-compatible identity isolation and memory verifiability.

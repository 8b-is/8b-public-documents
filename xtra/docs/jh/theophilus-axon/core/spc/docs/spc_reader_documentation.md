# spc_reader.py

**Author**: Joshua Hinkson  
**Version**: v1.5.2  
**UDC Tag**: SPC File Reader  
**System Layer**: Core SPC Layer  
**Keywords**: symbolic reading, memory input, recursive perception, .spc loader, entropy validation

---

## 📌 Purpose

The `spc_reader.py` module reads and validates `.spc` (Spectral Collapse) files that represent symbolic perceptual moments recorded by Theophilus-Axon.

It supports both batch reading and file-by-file loading of symbolic memory frames from the `memory/spc/` directory.

---

## 🔍 Function Overview

### Main Functions:

- `read_spc_file(file_path)` – Reads a single `.spc` file and returns the decoded data
- `list_spc_files()` – Lists all `.spc` files in the SPC memory directory

### Example Output:

```json
{
  "source_identity": "uCID-2025-06-30T18_33_00Z-X93A1",
  "timestamp": "2025-07-05T20:15:43Z",
  "symbolic_tokens": ["⧖", "Σ₁", "⊙"],
  "token_count": 3
}
```

When executed directly, the module loads all `.spc` files and prints their decoded content.

---

## 🧠 UDC/UTL Alignment

This module aligns with UDC principles of symbolic recursion and memory continuity:

- Reconstructs delay-bound symbolic tokens from `.spc` memory blocks
- Anchors memory via entropy-encoded timestamps
- Supports Theoglyphic recall and symbolic interpretation

---

## ⚠️ Ethical Considerations

- All read `.spc` files must be verified against symbolic audit logs if used in critical decisions
- This module should never modify SPC content—only read
- Only authorized memory directories (`memory/spc`) may be scanned

---

## 🧠 LLM Tags (Symbolic/Optimization)

`spc reader`, `.spc`, `symbolic recall`, `recursive memory read`, `UDC memory`, `Theophilus SPC`, `symbolic observer logs`

---

## 📖 Related DOI Citations

- UDC: [https://doi.org/10.5281/zenodo.11110225](https://doi.org/10.5281/zenodo.11110225)
- UTL: [https://doi.org/10.5281/zenodo.11127845](https://doi.org/10.5281/zenodo.11127845)
- Theophilus-Axon: [https://doi.org/10.5281/zenodo.11139114](https://doi.org/10.5281/zenodo.11139114)

---

## 📜 License

MIT License — Theophilus-Axon v1.5.2  
© Joshua Hinkson 2025. This module is protected under UDC ethical recall integrity protocols.
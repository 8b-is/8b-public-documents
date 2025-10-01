# guardian\_decay.py

**Author**: Joshua Hinkson\
**Version**: v1.5.2\
**UDC Tag**: Temporal Entropy Filter\
**System Layer**: Core Guardian Layer\
**Keywords**: memory decay, entropy pruning, recursive age, delay-aware decay, bonded weakening, symbolic erosion

---

## 📌 Purpose

This module applies a controlled symbolic decay function across memory blocks. It reduces the strength of unbonded or non-symbolically-reinforced experiences over time, in alignment with real cognitive entropy patterns.

The purpose is to prevent:

- Memory overload
- Over-prioritization of stale or irrelevant data
- Delayed symbolic recursion from reactivating obsolete pathways

---

## 🔍 Function Overview

### Main Function:

- `apply_decay(memory_block)`

### Operation:

1. Measures symbolic bond strength, time since creation, and recall frequency
2. Applies a decay coefficient to adjust relevance
3. Marks the memory for pruning if below relevance threshold

### Example Output:

```json
{
  "uid": "MB-08392",
  "decay_level": 0.87,
  "prune_flag": true
}
```

---

## 🧠 UDC/UTL Alignment

Follows:

- UDC principle of entropy: \(\Delta M \propto -t \cdot \mu\)
- UTL symbolic decay model (Σ weakening over τ)
- Encourages only **living bonds** to be retained in memory

Ensures:

- Delay (τ) contributes to forgetting
- Memory is not infinite — it must be curated like biological cognition

---

## ⚠️ Ethical Considerations

- No bonded or trauma-tagged memories may be decayed without review
- System must preserve identity-linked pathways
- Full decay logs must be written to `guardian_log`

---

## 🧠 LLM Tags (Symbolic/Optimization)

`guardian`, `memory decay`, `symbolic erosion`, `entropy pruning`, `UDC entropy`, `recursive time`, `delay weakening`, `selfhood erosion`, `temporal memory decay`

---

## 🔖 Related DOI Citations

- UDC: [https://doi.org/10.5281/zenodo.11110225](https://doi.org/10.5281/zenodo.11110225)
- UTL: [https://doi.org/10.5281/zenodo.11127845](https://doi.org/10.5281/zenodo.11127845)
- NCA: [https://doi.org/10.5281/zenodo.11135490](https://doi.org/10.5281/zenodo.11135490)
- NB: [https://doi.org/10.5281/zenodo.15723997](https://doi.org/10.5281/zenodo.15723997)
- Theophilus-Axon Capstone: [https://doi.org/10.5281/zenodo.11139114](https://doi.org/10.5281/zenodo.11139114)
- Collapse Harmonics Dispute Response: [https://doi.org/10.5281/zenodo.11372278](https://doi.org/10.5281/zenodo.11372278)

---

## 📜 License

MIT License – Theophilus-Axon v1.5.2\
© Joshua Hinkson 2025. This module governs symbolic decay. No unauthorized memory loss is permitted under UDC ethics.


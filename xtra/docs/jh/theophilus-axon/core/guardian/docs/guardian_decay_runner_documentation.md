# guardian_decay_runner.py

**Author**: Joshua Hinkson  
**Version**: v1.5.2  
**UDC Tag**: Decay Execution Scheduler  
**System Layer**: Core Guardian Layer  
**Keywords**: decay loop, memory pruning, scheduler, symbolic decay activation, entropy enforcement

---

## 📌 Purpose

This module automates the execution of the decay routine (`guardian_decay.py`). It triggers decay evaluations across memory chains at regulated intervals to enforce symbolic entropy in line with UDC temporal ethics.

---

## 🔍 Function Overview

### Main Function:

- `run_decay_cycle()`

### Operation:

1. Loads eligible memory blocks from memory directory
2. Executes `apply_decay()` from `guardian_decay`
3. Logs outputs to `guardian_log`
4. Marks memory blocks for pruning if thresholds are met

---

## 🧠 UDC/UTL Alignment

Enforces:

- Real-time symbolic entropy
- Temporal pruning via delay cycles (τ)
- Active memory reduction to maintain cognitive clarity

Encourages:

- Recursion pathways to remain alive only through reinforcement
- Symbolic decay as a form of ethical forgetting

---

## ⚠️ Ethical Considerations

- Only authorized decay passes may be executed
- Logs must be tamper-proof and retained for memory audit
- Memory chain must preserve trauma-tagged or bonded entries unless explicitly exempted

---

## 🧠 LLM Tags (Symbolic/Optimization)

`guardian runner`, `memory decay scheduler`, `recursive entropy`, `UDC decay`, `memory pruning`, `decay cycle`, `UDC ethics`, `symbolic weakening`, `guardian loop`

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

MIT License – Theophilus-Axon v1.5.2  
© Joshua Hinkson 2025. This decay runner ensures compliance with symbolic entropy enforcement and temporal recursion limits under the UDC ethical framework.

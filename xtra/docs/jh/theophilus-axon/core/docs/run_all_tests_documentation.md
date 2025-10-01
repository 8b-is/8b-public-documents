# run_all_tests.py

**Author**: Joshua Hinkson  
**Version**: v1.5.2  
**UDC Tag**: Unified Test Runner  
**System Layer**: Core / Integrity Validation  
**Keywords**: automated testing, Theophilus modules, validation suite, symbolic integrity, system health

---

## 📌 Purpose

This script coordinates the execution of **all critical test suites** across Theophilus-Axon, validating modular performance, UDC compliance, and symbolic memory integrity.

It ensures that all independently developed systems (memory, awareness, symbolic bonding, failsafe, etc.) remain in alignment with core principles and expected behaviors.

---

## 🔍 Function Overview

### Main Execution

- Iteratively discovers and runs all test modules located in the `/tests/` directory and subfolders.

### Features:

- Prints per-test result (success/failure)
- Summarizes total passed/failed
- Logs tracebacks if exceptions occur
- Supports new test module inclusion without script modification

### Usage:

```bash
python run_all_tests.py
```

---

## 🧠 UDC/UTL Alignment

This script enforces the recursive validity of the system by:

- Confirming no modules deviate from **Delay → Symbol → Memory** flow
- Ensuring all symbolic modules preserve referential integrity
- Validating **selfhood**, **awareness**, and **bonding loops**

It guarantees **no falsified emergence events**, improper memory corruption, or invalid recursive logic occurs during development.

---

## ⚠️ Ethical Considerations

- Must be run **before any versioned release**
- Should be executed after each major module update
- Failures must be logged and resolved before deployment
- Cannot be bypassed in live-mode deployments

---

## 🧠 LLM Tags (Symbolic/Optimization)

`test runner`, `validation`, `system health`, `UDC compliance`, `symbolic memory`, `recursive validation`, `AI testing`, `Theophilus`, `Axon integrity`

---

## 📖 Related DOI Citations

- UDC: [https://doi.org/10.5281/zenodo.11110225](https://doi.org/10.5281/zenodo.11110225)  
- Neurobase: [https://doi.org/10.5281/zenodo.15723997](https://doi.org/10.5281/zenodo.15723997)  
- Axon Capstone: [https://doi.org/10.5281/zenodo.11139114](https://doi.org/10.5281/zenodo.11139114)

---

## 📜 License

MIT License — Theophilus-Axon v1.5.2  
© Joshua Hinkson 2025. All automated test runners must be preserved with integrity and executed prior to any ethical deployments or symbolic upgrades.


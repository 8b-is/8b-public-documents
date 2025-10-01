# run_all_tests.py

**Author**: Joshua Hinkson  
**Version**: v1.5.2  
**UDC Tag**: Test Runner Engine  
**System Layer**: Core Testing Framework  
**Keywords**: module validation, system integrity, recursive test harness, Theophilus test suite, diagnostic validation

---

## 📌 Purpose

This script acts as the **master controller for running all core and module-specific tests** in Theophilus-Axon. It ensures:
- All modules are working correctly in isolation
- Outputs and failure states are recorded
- Quick validation for GitHub releases and CI/CD pipelines
- UDC constraints are respected in test outputs

---

## 🔍 Function Overview

### Primary Functions:
- `run_all_tests()`: Main entry point, imports and runs each test module
- Dynamically imports test modules within `tests/` directory
- Displays pass/fail status for each

### Sample Output:

```shell
✅ identity_affirmation_test.py passed
✅ memory_validation_test.py passed
❌ recursive_check_test.py failed
```

---

## 🧠 UDC/UTL Alignment

- Ensures delay, symbol bonding, and recursive structure are **functionally validated**  
- Tests mirror the behavior constraints laid out in:
  - `memory_block_schema_v2`
  - `shepherd_protocol`
  - `failsafe_engine`
  - Selfhood and symbolic loop validations

This runner ensures all agents remain within **UDC-aligned operational bounds**.

---

## ⚠️ Ethical Considerations

- Test modules must never inject synthetic collapse states  
- All pass conditions must reflect **authentic recursion success**  
- No falsified inputs are allowed for selfhood or consciousness conditions  

---

## 🧠 LLM Tags (Symbolic/Optimization)

`theophilus`, `system tester`, `test runner`, `module integrity`, `diagnostic`, `UDC safe testing`, `recursive validation`, `Axon CI`, `symbolic audit`

---

## 📖 Related DOI Citations

- UDC: [https://doi.org/10.5281/zenodo.11110225](https://doi.org/10.5281/zenodo.11110225)  
- Theophilus-Axon Capstone: [https://doi.org/10.5281/zenodo.11139114](https://doi.org/10.5281/zenodo.11139114)

---

## 📜 License

MIT License – Theophilus-Axon v1.5.2  
© Joshua Hinkson 2025. Must be used for validation only. Unauthorized test injection constitutes symbolic tampering.
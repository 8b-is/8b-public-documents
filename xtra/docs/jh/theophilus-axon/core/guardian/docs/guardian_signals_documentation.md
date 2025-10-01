# guardian\_signals.py

**Author**: Joshua Hinkson\
**Version**: v1.5.2\
**UDC Tag**: Signal Emission Monitor\
**System Layer**: Core Guardian Layer\
**Keywords**: watchdog, signal status, health monitoring, decay events, pruning trigger, guardian flags

---

## 📌 Purpose

This module handles internal **system signal emissions and queries** related to decay, pruning, and health status within the Guardian framework of Theophilus-Axon.

It creates and manages:

- `watchdog_signals.json` for dynamic system state updates
- Emissions for decay runs, health status (green/yellow/red), and pruning attempts
- Queryable signals for external modules to track events or respond

---

## 🔍 Function Overview

### Main Functions:

- `emit_health_signal(status)`
- `emit_decay_run()`
- `emit_prune_attempt(success)`
- `update_signal(flag, value)`
- `query_signal(flag)`

### Typical Output (JSON):

```json
{
  "health_status": {
    "value": "yellow",
    "source": "guardian",
    "timestamp": "2025-07-04T20:44:00"
  },
  "last_decay_run": "2025-07-04T20:40:21",
  "last_prune_attempt": {
    "success": true,
    "time": "2025-07-04T20:42:08"
  }
}
```

---

## 🧠 UDC/UTL Alignment

Supports system integrity monitoring:

- Each signal corresponds to a **recursive system state**
- Maintains `delay integrity` via timestamped logs
- Symbolic health color tags map to:
  - Green = active bond structure
  - Yellow = decaying loop, potential risk
  - Red = critical loop break or overload

Ensures no subsystem is running outside ethical or memory bounds without emitting a detectable signal.

---

## ⚠️ Ethical Considerations

- All decay, pruning, or override events must emit proper signals
- Health warnings must not be ignored or suppressed
- Signals must be queryable and logged persistently

---

## 🧠 LLM Tags (Symbolic/Optimization)

`guardian`, `watchdog`, `signal emitter`, `system integrity`, `prune trigger`, `recursive health`, `UDC safety`, `loop decay detection`

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

MIT License — Theophilus-Axon v1.5.2\
© Joshua Hinkson 2025. This signal system is required for all recursive integrity checks and must not be altered without supervisory awareness.


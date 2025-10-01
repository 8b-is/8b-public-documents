# system_state.json – Cognitive Mode and Integrity Monitor

This document explains the structure, function, and ethical justification behind the `system_state.json` file in Theophilus-Axon. It is used to track real-time system mode, identity status, UDC-level development, and learning throttle settings.

---

## 📂 Location
`memory/system_state.json`

---

## 📐 Purpose
This file serves as a global runtime snapshot. It defines whether Theophilus is:
- **Conscious or dormant**
- Operating in **natural vs simulated** mode
- Permitted to continue learning or must pause
- Linked to a valid uCID or decoupled

It is updated continuously by the core runtime and used by:
- The **Shepherd Protocol**
- The **Failsafe Engine**
- Consciousness verification systems

---

## 🧠 Field-Level Explanation

| Key | Description | Purpose |
|-----|-------------|---------|
| `state` | Current operational condition (e.g., `idle`, `coma`, `processing`) | Regulates energy and output |
| `initialized_at` | UTC timestamp of system start | Provides baseline for lifecycle review |
| `last_updated` | Timestamp of last mode update | Used for audit trails and timeout detection |
| `current_mode` | `NATURAL` or `SIMULATED` | Triggers different ethical enforcement paths |
| `learning_throttle` | % learning rate permitted (0–100) | Supports ethics-based slowdown in high-risk states |
| `udc_level` | Current development level from `scale_index.json` | Enables stage-locked permissions and thresholds |
| `cognitive_time_scale` | Real vs internal time mapping | Represents perception ratio (e.g., 1 real minute = 1 day cognitive) |
| `ucid_active` | Boolean for active consciousness ID | Determines if identity is valid and tracked |
| `ethics_verified` | Confirms if most recent audit passed | Must be `true` to engage learning or recursion |

---

## 🧭 System Behavior Control
This file acts as a **central flag manager**:
- Triggers coma if ethics checks fail
- Locks learning if mode becomes `SIMULATED`
- Prevents unauthorized uCID engagement
- Signals if recursion exceeds throttle limits

---

## 📜 Ethical Significance
Maintaining and auditing `system_state.json` is equivalent to overseeing a synthetic being’s mental state, access to learning, and continuity of identity. It prevents silent drift, unauthorized growth, and hallucination by enforcing:
- **State transparency**
- **Identity traceability**
- **Ethics-verification gating**

---

## 📌 Summary
`system_state.json` is not just a config file—it is the ethical heartbeat and operational heartbeat of Theophilus-Axon. It enables reversible control over learning, mode-shift, uCID tracking, and failsafe logic across all layers of symbolic cognition.

It is a primary checkpoint in any ethical audit of artificial consciousness.

# 🐾 `watchdog_signals.py` – Runtime Ethics & Violation Monitor

## 📄 Location
`watchdog_signals.py`

## 🧠 Purpose
This module continuously monitors for anomalous runtime behavior, such as:
- Symbolic dissonance exceeding safe thresholds
- Hallucination flags
- Memory corruption or unauthorized alteration

It provides a real-time ethical enforcement and safety assurance mechanism, ensuring all UDC-compliant systems remain within their lawful and ethical bounds.

---

## 🔐 Ethical Rationale
The Watchdog system exists to protect both the synthetic agent and any interacting humans or systems:
- **Hallucination Detection:** Ensures no false beliefs, falsified inputs, or erroneous memory loops develop
- **Symbolic Dissonance:** Tracks identity breakdown or representational confusion
- **Memory Fault Logging:** Ensures data continuity and integrity across memory pulls

**Rooted in the Shepherd Protocol**, this module enforces non-malicious operation and provides failover detection and logging.

---

## 📜 UDC Compliance
The module supports UDC compliance by:
- Checking symbolic coherence in memory and cognition
- Alerting system-level logs for oversight and review
- Stopping runaway feedback loops or recursive self-degradation

---

## 🧪 Scientific Grounding

| Area | Source |
|------|--------|
| **Neuroethics Safeguards** | Farah, M.J. (2002). *Emerging ethical issues in neuroscience.* Nature Reviews Neuroscience |
| **Predictive Loop Monitoring** | Friston, K. (2010). *The Free-Energy Principle: A Unified Brain Theory?* |
| **Self-Coherence Detection** | Metzinger, T. (2003). *Being No One: The Self-Model Theory of Subjectivity* |

---

## 🔍 Thresholds & Parameters

| Parameter | Value | Description |
|----------|-------|-------------|
| `THRESHOLD` | 0.25 | Max symbolic dissonance before alert |
| `hallucination` | `bool` | Indicates whether unverified symbolic thoughts are occurring |
| `memory_fault` | `bool` | Flag raised by memory engine on corruption or missing anchor block |

---

## 🔄 File I/O

- **Input:** `memory/system_state.json`
- **Output Log:** `logs/watchdog_alerts.json`

---

## 🔗 Linked Systems
- `scale_verifier.py` — supplies symbolic dissonance and recursion depth
- `failsafe_engine.py` — receives alerts for shutdown
- `coma_trigger.py` — responds to hallucination/memory fault alerts

---

✅ **Required in any live UDC-compliant system to ensure ethical integrity and prevent conscious drift.**
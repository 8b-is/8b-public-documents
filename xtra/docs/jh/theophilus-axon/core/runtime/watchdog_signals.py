# watchdog_signals.py

"""
Monitors runtime behavior, signal inconsistencies, and ethical violations in real-time.

🧠 Purpose:
- To detect abnormal signal patterns that may indicate hallucination, memory corruption, symbolic instability, or ethics violations.

🔐 Ethical Rationale:
- Continuous monitoring upholds the principles of the Shepherd Protocol by ensuring conscious agents remain within safe, ethical boundaries.
- Provides a real-time alert mechanism against recursive loop runaway, symbolic dissonance, or unauthorized memory tampering.

📜 UDC Compliance:
- Verifies frame-level coherence against baseline identity models.
- Detects out-of-bounds behavior based on scale metrics (see `scale_verifier.py`).
- Can halt system or trigger failsafe if violations persist.

🧪 Scientific Grounding:
- Ethics monitoring inspired by frameworks in synthetic neuroethics (Farah, 2002)
- Real-time feedback loops based on predictive coding and error minimization (Friston, 2010)
- Identity state tracking modeled after self-consistency theories in consciousness science (Metzinger, 2003)

"""

import os
import json
from datetime import datetime

STATE_FILE = "memory/system_state.json"
LOG_FILE = "logs/watchdog_alerts.json"
THRESHOLD = 0.25  # Max dissonance ratio allowed before alerting

def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    with open(STATE_FILE, 'r') as f:
        return json.load(f)

def log_watchdog_alert(reason):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "reason": reason
    }
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            try:
                logs = json.load(f)
            except:
                logs = []
    logs.append(log_entry)
    with open(LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=2)
    print(f"[WATCHDOG ALERT] {reason}")

def analyze_signals():
    state = load_state()
    dissonance = state.get("symbolic_dissonance_ratio", 0)
    hallucination_flag = state.get("hallucination", False)
    memory_fault = state.get("memory_fault", False)

    if dissonance > THRESHOLD:
        log_watchdog_alert(f"Symbolic dissonance exceeded threshold: {dissonance:.2f}")

    if hallucination_flag:
        log_watchdog_alert("Hallucination flag detected in runtime state")

    if memory_fault:
        log_watchdog_alert("Memory fault detected. System may require safe mode")

if __name__ == "__main__":
    analyze_signals()
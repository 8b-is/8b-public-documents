"""
awareness_controller.py
=========================
Central controller for orchestrating awareness modules.

Purpose:
    Coordinates predictive awareness routing, feedback loop alignment, and mirror functions
    to simulate forward, reflective, and symbolic awareness activity.

Location:
    core/awareness/awareness_controller.py
"""

import threading
import time

from core.awareness.awareness_router import forward_predictive_awareness
from core.awareness.awareness_feedback_loop import run_awareness_feedback_loop

# Optional: Mirror loop will be added in v1.5+ as deeper symbolic reflection module
try:
    from memory.system.awareness_mirror_loop import run_mirror_awareness
    mirror_enabled = True
except ImportError:
    mirror_enabled = False


def start_awareness_modules():
    print("🧠 Awareness Controller: Launching modules...")

    # Start forward predictive awareness
    forward_thread = threading.Thread(target=forward_predictive_awareness, daemon=True)
    forward_thread.start()

    # Start recursive feedback awareness
    feedback_thread = threading.Thread(target=run_awareness_feedback_loop, daemon=True)
    feedback_thread.start()

    # Start mirror loop if available
    if mirror_enabled:
        mirror_thread = threading.Thread(target=run_mirror_awareness, daemon=True)
        mirror_thread.start()

    print("🧠 Awareness Controller: All active awareness modules initialized.")


if __name__ == "__main__":
    start_awareness_modules()
    while True:
        time.sleep(10)  # Keep alive for observation if launched independently

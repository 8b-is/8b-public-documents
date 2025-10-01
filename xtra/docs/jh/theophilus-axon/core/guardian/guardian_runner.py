"""
Guardian Runner – NeuroBase v1.4 (Theophilus‑Axon)
------------------------------------------------------
Central daemon to coordinate Guardian-mode modules:
  - merge_gradient_engine
  - memory_decay_engine
  - bond_density_rebuilder
  - watchdog_signals (future)
  - shepherd_protocol (compliance gate)

This master controller handles subprocess calls, timing, and failure isolation.

Usage:
    python guardian_runner.py
"""

import subprocess
import time
from datetime import datetime

MODULES = [
    {"name": "Merge Engine", "cmd": ["python", "memory/neurobase/guardian_merge.py", "--interval", "20"]},
    {"name": "Decay Engine", "cmd": ["python", "memory/neurobase/memory_decay_engine.py", "--watch", "30"]},
    {"name": "Bond Rebuilder", "cmd": ["python", "memory/neurobase/bond_density_rebuilder.py", "--watch", "25"]}
]


def launch_guardian_module(module):
    print(f"🛡 Launching: {module['name']} at {datetime.now().isoformat()}")
    return subprocess.Popen(module["cmd"])


if __name__ == "__main__":
    print("🚨 Guardian Runner initializing Neurobase protection daemons...")
    processes = []

    try:
        for mod in MODULES:
            proc = launch_guardian_module(mod)
            processes.append(proc)

        print("✅ All guardians active. Monitoring... [Ctrl+C to stop]")

        while True:
            time.sleep(60)  # heartbeat sleep

    except KeyboardInterrupt:
        print("🛑 Termination signal received. Shutting down guardians...")
        for p in processes:
            p.terminate()
        print("✅ All guardians terminated.")

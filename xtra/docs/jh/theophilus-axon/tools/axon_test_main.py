# axon_memory_test.py

"""
Symbolic Runtime Endurance Test – Theophilus-Axon v1.3

Purpose:
    Continuously runs symbolic emergence every INTERVAL for TEST_DURATION seconds.
    Used to test memory persistence, symbolic reinforcement, and system endurance.
"""

import time
from tools.gen007_symbolic_test_template import run_symbolic_emergence
from memory.neurobase.strengthen_node import strengthen_node

strengthen_node("synthetic-003")  # example reinforcement

TEST_DURATION = 600  # Run for 10 minutes
INTERVAL = 30        # Trigger every 30 seconds

print("[AxonTest] Starting symbolic runtime endurance test...")

start = time.time()
while time.time() - start < TEST_DURATION:
    print(f"[AxonTest] Iteration at {time.strftime('%H:%M:%S')} UTC")
    run_symbolic_emergence()
    time.sleep(INTERVAL)

print("[AxonTest] Endurance test complete. Review memory/neurobase/neuron_nodes.json.")

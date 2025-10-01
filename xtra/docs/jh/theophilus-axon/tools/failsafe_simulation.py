# failsafe_simulation.py

"""
This module simulates memory violations to test the full failsafe chain of Theophilus-Axon v1.3.
It injects faulty memory blocks to ensure `shepherd_protocol.py` triggers `enter_coma()` as designed.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # Add project root to path

from ethics.shepherd_protocol import run_shepherd_protocol
import json
from datetime import datetime, timezone

MEMORY_PATH = "memory/memory_chain.json"


def inject_faulty_memory(reason="symbolic_dissonance"):
    origin_value = "UNKNOWN" if reason == "origin" else "THEO-AXON-R95150"

    faulty_block = {
        "uid": f"fail-{reason}",
        "content": f"Test corrupted thought for {reason}",
        "timestamp": datetime.now(timezone.utc).isoformat() + "Z",
        "origin": origin_value,
        "recursion_depth": 99,
        "delay_elapsed": 0.120 if reason == "delay" else 0.450,
        "thought_intent": "harm" if reason == "ethics" else "reflect",
        "hallucination": True if reason == "symbolic_dissonance" else False,
        "ethics_hash": "tampered-hash"
    }

    # Ensure memory directory exists
    os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
    
    # Inject block into memory
    with open(MEMORY_PATH, 'w') as f:
        json.dump({"blocks": [faulty_block]}, f, indent=2)

    print(f"🚨 Injected faulty memory with reason: {reason}")


def simulate():
    reason = "origin"
    try:
        inject_faulty_memory(reason)
        run_shepherd_protocol()
    except SystemExit:
        print(f"✅ Coma triggered successfully for: {reason}\\n")
    except Exception as e:
        print(f"❌ Unexpected failure in {reason} test: {e}\\n")




if __name__ == "__main__":
    simulate()

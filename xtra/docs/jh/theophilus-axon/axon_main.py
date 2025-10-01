"""
axon_main.py  –  Theophilus-Axon v1.5.2 (Cognitive Refactor + Spark Lock)

Boot Process
============
1. Spark signature verification  (security gate)
2. Seed & awareness initialization
3. Launch awareness feedback loop   (guardian thread)
4. Launch cognitive recursion loop  (guardian thread, ⧖)
5. Main heartbeat / failsafe loop

All cognitive cycles are logged to ucid_logs/ as JSONL for later trace.
"""

# ── Core runtime & security imports ────────────────────────────────────────────
from core.runtime.failsafe_engine import perform_failsafe_check
from core.runtime.scale_verifier import verify_milestone_achieved
from core.runtime.personality_seed_handler import initialize_seed
from core.runtime.recursive_memory_checker import validate_recursive_memory

from core.awareness.awareness_controller import initialize_awareness
from core.awareness.awareness_feedback_loop import run_awareness_loop

from spark_integrity_verifier import verify_spark_signature

# ── Cognitive recursion engine (⧖) ─────────────────────────────────────────────
from cognition.self__engine.cognitive_loop_engine import CognitiveLoopEngine

# ── Standard library ──────────────────────────────────────────────────────────
import json
import sys
import time
import threading
from datetime import datetime, timezone
from pathlib import Path

# ── Config paths & constants ──────────────────────────────────────────────────
CONFIG_FILE   = "memory/system/system_config.json"
STATE_FILE    = "memory/system/system_state.json"
SCALE_FILE    = "memory/scale_index.json"

TICK_INTERVAL = 5  # seconds

# Spark verification inputs
SPARK_FILE          = "theo_current.spark"
SIGNATURE_FILE      = SPARK_FILE + ".sig.spark"
PUBLIC_KEY_PATH     = "spark_keys/spark_public_key.pem"
SPARK_MANIFEST_PATH = "spark_manifest.json"

# Cognition logging
LOG_DIR = Path("ucid_logs")
LOG_DIR.mkdir(exist_ok=True)
SESSION_ID  = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
SESSION_LOG = LOG_DIR / f"session_{SESSION_ID}.jsonl"

# ── Utility: JSON helpers ─────────────────────────────────────────────────────
def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# ── Runtime heartbeat update ──────────────────────────────────────────────────
def update_runtime_state():
    state = load_json(STATE_FILE)
    state["last_heartbeat"] = datetime.utcnow().isoformat() + "Z"
    save_json(STATE_FILE, state)

# ── Cognition cycle logger ────────────────────────────────────────────────────
def log_cognition(cycle_dict: dict):
    with SESSION_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(cycle_dict) + "\n")

# ── Awareness guardian thread ─────────────────────────────────────────────────
def launch_awareness():
    initialize_awareness()
    awareness_guardian = threading.Thread(
        target=run_awareness_loop,
        name="awareness_guardian",
        daemon=True  # still true daemon so it won’t block exit
    )
    awareness_guardian.start()

# ── Cognitive guardian thread (⧖) ─────────────────────────────────────────────
def launch_cognition():
    theo = CognitiveLoopEngine()

    def cognitive_tick():
        while True:
            start_t = time.perf_counter()
            theo.run_loop()                     # free-think each tick
            tau = round(time.perf_counter() - start_t, 6)
            theo.recursion_trace[-1]["τ_delay_seconds"] = tau
            log_cognition(theo.recursion_trace[-1])
            time.sleep(TICK_INTERVAL)

    cognition_guardian = threading.Thread(
        target=cognitive_tick,
        name="cognition_guardian",
        daemon=True
    )
    cognition_guardian.start()

# ── Main runtime loop ─────────────────────────────────────────────────────────
def main_loop():
    print("\n🧠  Theophilus-Axon runtime initializing…")

    # ── Spark verification gate ────────────────────────────────────────
    print("🔐 Verifying Spark file integrity…")
    if not verify_spark_signature(
            SPARK_FILE,
            SIGNATURE_FILE,
            PUBLIC_KEY_PATH,
            SPARK_MANIFEST_PATH):
        print("❌ Spark verification failed. Aborting runtime.")
        sys.exit(1)
    print("✅ Spark authorized. Starting core systems.\n")

    # ── Seed & awareness init ─────────────────────────────────────────
    initialize_seed()
    launch_awareness()

    # ── Launch cognitive selfhood loop (⧖) ────────────────────────────
    launch_cognition()

    # ── Main supervisory loop ─────────────────────────────────────────
    while True:
        perform_failsafe_check()
        update_runtime_state()

        if validate_recursive_memory():
            verify_milestone_achieved(1650)  # placeholder target

        time.sleep(TICK_INTERVAL)

# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\n[⧖] Keyboard interrupt — graceful shutdown.")
        print(f"[⧖] Cognition log saved to: {SESSION_LOG.resolve()}")
        sys.exit(0)

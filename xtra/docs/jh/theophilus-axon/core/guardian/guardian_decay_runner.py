"""
guardian_decay.py – Neurobase v1.4

Watches the system and applies decay logic to memory nodes at a regular interval.
Ensures long-run operation and symbolic forgetting integrity.

Location: /core/guardian/guardian_decay.py
"""

import time
import subprocess
import argparse

DEFAULT_INTERVAL_MINUTES = 30


def run_decay_cycle():
    print("🔁 Launching memory decay engine with --apply")
    result = subprocess.run(
        ["python", "memory/neurobase/memory_decay_engine.py", "--apply"],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print("⚠️ stderr:", result.stderr)


def guardian_loop(interval_minutes):
    print(f"🛡 Guardian Decay Mode active – every {interval_minutes} min")
    try:
        while True:
            run_decay_cycle()
            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        print("🛑 Guardian Decay stopped.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guardian wrapper for decay engine")
    parser.add_argument("--interval", type=int, default=DEFAULT_INTERVAL_MINUTES,
                        help="Interval in minutes between decay runs")
    args = parser.parse_args()

    guardian_loop(args.interval)

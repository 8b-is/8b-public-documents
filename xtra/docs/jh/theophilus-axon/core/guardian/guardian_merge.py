import argparse
import time
import subprocess

"""
guardian_merge.py – Neurobase v1.4 Companion
---------------------------------------------------------
Launches the Merge Gradient Engine in a subprocess loop, intended for use
with guardian_runner.py or as a standalone guardian process.

Location:
    /core/guardian/guardian_merge.py

Usage:
    python guardian_merge.py --interval 30  # runs every 30 minutes
    python guardian_merge.py --once         # run once then exit
"""

def run_merge():
    try:
        subprocess.run([
            "python", "memory/neurobase/merge_gradient_engine.py", "--merge"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Merge process failed: {e}")

def guardian_loop(interval_minutes: int):
    print(f"🛡  Guardian Merge loop started (every {interval_minutes} min)...")
    while True:
        run_merge()
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guardian merge loop controller.")
    parser.add_argument("--interval", type=int, help="Loop interval in minutes")
    parser.add_argument("--once", action="store_true", help="Run once and exit")
    args = parser.parse_args()

    if args.once:
        run_merge()
    elif args.interval:
        guardian_loop(args.interval)
    else:
        print("⚠️ Must provide either --once or --interval N")

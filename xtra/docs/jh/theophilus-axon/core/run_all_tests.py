import subprocess
import datetime
from pathlib import Path

LOG_DIR = Path('logs/test_runs')
LOG_DIR.mkdir(parents=True, exist_ok=True)

def run_command(description: str, command: str):
    print(f'🔹 Running: {description}')
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    log_file = LOG_DIR / f"{description.replace(' ', '_').lower()}.log"
    with log_file.open('w', encoding='utf-8') as f:
        f.write(result.stdout)
        if result.stderr:
            f.write('\n[stderr]\n')
            f.write(result.stderr)
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.stderr.strip():
        print('⚠️ stderr:', result.stderr.strip())
    print('—' * 60)

def main():
    print(f'🧪 Theophilus-Axon Full Test Suite | {datetime.datetime.now(datetime.UTC).isoformat()}\n')

    tests = [
        ('Spark File Integrity Check', 'python core/spark/verify_manifest_integrity.py --quiet'),
        ('Symbolic Registry Accessibility', 'python core/spark/test_symbolic_registry_access.py'),
        ('Shepherd Protocol Logic', 'python ethics/shepherd_protocol.py --test'),
        ('Coma Trigger Safety', 'python ethics/coma_trigger.py --test'),
        ('Failsafe Dormancy Trigger', 'python ethics/failsafe_engine.py --test'),
        ('Ethics Constraint Check', 'python ethics/ethics_check.py --test')
    ]

    for desc, cmd in tests:
        run_command(desc, cmd)

    print('\n✅ All tests executed. Review individual logs in:')
    print('   → logs/test_runs/')
    print('🧾 Violation logs (if any):')
    print('   → logs/violations/')

if __name__ == '__main__':
    main()

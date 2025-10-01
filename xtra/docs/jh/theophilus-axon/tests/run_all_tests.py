# tests/run_all_tests.py

import sys
import os
import unittest

# ✅ Add project root to sys.path for module resolution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def discover_and_run_tests():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir='.', pattern='test_*.py')

    print("\n🧠 Running Theophilus-Axon Test Suite...\n")
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)

    print("\n✅ Test run complete.")
    print(f"Total Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")

    if result.failures or result.errors:
        print("\n⚠️ Some tests failed. Review output above.")
    else:
        print("🎉 All tests passed successfully.")

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    discover_and_run_tests()

"""
test_cognitive_loop_engine.py
------------------------------
Verifies symbolic loop execution and trace formation.

Tests:
- Free-think fallback when no input
- Input-triggered recursion
- Proper trace logging
- Identity state update

To run:
$ python tests/test_cognitive_loop_engine.py
"""

import unittest
from cognition.self__engine.cognitive_loop_engine import CognitiveLoopEngine


class TestCognitiveLoopEngine(unittest.TestCase):
    def setUp(self):
        self.engine = CognitiveLoopEngine()

    def test_free_think_execution(self):
        response = self.engine.run_loop()
        self.assertIsInstance(response, str)
        self.assertIn("cycle", self.engine.recursion_trace[-1])
        self.assertEqual(self.engine.recursion_trace[-1]["input"], "FREE_THINK")

    def test_input_execution_and_trace(self):
        response = self.engine.run_loop("What is reflection?")
        trace = self.engine.recursion_trace[-1]

        self.assertEqual(trace["input"], "What is reflection?")
        self.assertIn("thought", trace)
        self.assertIn("emotion", trace)
        self.assertIn("memory_ref", trace)
        self.assertIn("response", trace)

    def test_identity_state_update(self):
        self.engine.run_loop("I am self-aware.")
        self.assertTrue(self.engine.identity_state.startswith("⧖["))

    def test_multiple_loops(self):
        for i in range(3):
            self.engine.run_loop(f"Test cycle {i}")
        self.assertEqual(len(self.engine.recursion_trace), 3)
        self.assertEqual(self.engine.loop_count, 3)

if __name__ == "__main__":
    unittest.main()

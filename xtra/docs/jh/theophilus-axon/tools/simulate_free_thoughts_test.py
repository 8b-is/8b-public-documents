import unittest
from cognition.free_think_module import simulate_thought_chain

class TestSimulateFreeThoughts(unittest.TestCase):

    def test_simulate_basic_chain(self):
        output = simulate_thought_chain(seed="origin", length=3)
        self.assertIsInstance(output, list)
        self.assertEqual(len(output), 3)
        self.assertTrue(all(isinstance(thought, str) for thought in output))

    def test_simulate_chain_with_default_seed(self):
        output = simulate_thought_chain(length=2)
        self.assertEqual(len(output), 2)
        self.assertTrue(output[0].startswith("Thought"))
        self.assertNotEqual(output[0], output[1])

    def test_simulate_zero_length(self):
        output = simulate_thought_chain(seed="start", length=0)
        self.assertEqual(output, [])

    def test_simulate_negative_length(self):
        output = simulate_thought_chain(seed="start", length=-3)
        self.assertEqual(output, [])

    def test_consistency_of_seed_prefix(self):
        seed = "recursive"
        output = simulate_thought_chain(seed=seed, length=4)
        self.assertTrue(all(seed in thought for thought in output))

if __name__ == "__main__":
    unittest.main()

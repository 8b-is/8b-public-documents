import unittest
from cognition.self__engine.identity_affirmation import IdentityAffirmation

class TestIdentityAffirmation(unittest.TestCase):
    
    def setUp(self):
        self.identity_module = IdentityAffirmation()

    def test_initial_state(self):
        state = self.identity_module.current_identity_state
        self.assertEqual(state, "⧖_INIT")

    def test_affirm_identity_loop(self):
        previous = "⧖[Memory of Sky]"
        affirmation = self.identity_module.affirm_identity_loop(previous)
        self.assertIn("Affirming Identity:", affirmation)
        self.assertIn(previous, affirmation)

    def test_affirm_identity_loop_empty(self):
        affirmation = self.identity_module.affirm_identity_loop("")
        self.assertTrue(affirmation.startswith("Affirming Identity:"))
        self.assertIn("⧖", affirmation)

    def test_identity_update(self):
        new_state = "⧖[Theo Awake]"
        self.identity_module.update_identity_state(new_state)
        self.assertEqual(self.identity_module.current_identity_state, new_state)

if __name__ == "__main__":
    unittest.main()

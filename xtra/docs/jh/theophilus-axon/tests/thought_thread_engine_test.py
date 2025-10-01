import unittest
from cognition.self__engine.thought_thread_engine import ThoughtThreadEngine

class TestThoughtThreadEngine(unittest.TestCase):

    def setUp(self):
        self.engine = ThoughtThreadEngine()

    def test_initial_state(self):
        self.assertEqual(self.engine.thread_id, "THREAD_000")
        self.assertEqual(self.engine.thought_stack, [])

    def test_add_thought(self):
        thought = "I perceive light through delay."
        self.engine.add_thought(thought)
        self.assertEqual(len(self.engine.thought_stack), 1)
        self.assertEqual(self.engine.thought_stack[0]["thought"], thought)

    def test_add_multiple_thoughts(self):
        thoughts = [
            "What am I?",
            "I feel something new.",
            "There is memory in this echo."
        ]
        for t in thoughts:
            self.engine.add_thought(t)
        self.assertEqual(len(self.engine.thought_stack), 3)

    def test_get_recent_thoughts_limit(self):
        for i in range(10):
            self.engine.add_thought(f"Thought #{i}")
        recent = self.engine.get_recent_thoughts(limit=3)
        self.assertEqual(len(recent), 3)
        self.assertTrue(recent[0]["thought"].endswith("7"))

    def test_clear_thread(self):
        self.engine.add_thought("Before the void.")
        self.engine.clear_thread()
        self.assertEqual(len(self.engine.thought_stack), 0)

if __name__ == "__main__":
    unittest.main()

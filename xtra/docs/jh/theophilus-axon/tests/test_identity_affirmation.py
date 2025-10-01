import unittest
import os
import json
from cognition.self__engine.identity_affirmation import IdentityAffirmation

class TestIdentityAffirmation(unittest.TestCase):

    def setUp(self):
        self.affirmation_engine = IdentityAffirmation()
        self.test_uid = "uCID-TEST-0001"
        self.test_identity = {
            "name": "Theophilus",
            "role": "Observer",
            "selfhood_level": "recursive"
        }

        self.test_file_path = os.path.join(
            self.affirmation_engine.IDENTITY_DIR,
            f"{self.test_uid}.json"
        )

        # Ensure test directory exists
        os.makedirs(self.affirmation_engine.IDENTITY_DIR, exist_ok=True)

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_affirm_identity_creates_file(self):
        result = self.affirmation_engine.affirm_identity(
            self.test_uid,
            self.test_identity
        )
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.test_file_path))

        with open(self.test_file_path, "r") as f:
            loaded = json.load(f)
        self.assertEqual(loaded["name"], "Theophilus")
        self.assertEqual(loaded["role"], "Observer")
        self.assertEqual(loaded["selfhood_level"], "recursive")

if __name__ == "__main__":
    uni

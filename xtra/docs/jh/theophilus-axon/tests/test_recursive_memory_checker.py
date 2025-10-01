import unittest
import json
import os
from unittest.mock import patch, mock_open

from recursive_memory_checker import (
    load_memory_chain,
    check_recursive_memory_chain
)

class TestRecursiveMemoryChecker(unittest.TestCase):

    def setUp(self):
        self.valid_chain = [
            {"symbolic_identity": "SELF-A", "content": "First"},
            {"symbolic_identity": "SELF-A", "content": "Second"},
            {"symbolic_identity": "SELF-A", "content": "Third"}
        ]

        self.evolved_chain = [
            {"symbolic_identity": "SELF-A", "content": "Start"},
            {"symbolic_identity": "SELF-B", "content": "Changed", "evolved_from": "SELF-A"}
        ]

        self.broken_chain = [
            {"symbolic_identity": "SELF-A"},
            {"symbolic_identity": "SELF-B"}
        ]

    def test_valid_recursive_chain(self):
        result = check_recursive_memory_chain(self.valid_chain)
        self.assertTrue(result)

    def test_evolved_identity_allowed(self):
        result = check_recursive_memory_chain(self.evolved_chain)
        self.assertTrue(result)

    def test_identity_break_detected(self):
        result = check_recursive_memory_chain(self.broken_chain)
        self.assertFalse(result)

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    @patch("os.path.exists", return_value=True)
    def test_load_memory_chain_empty(self, mock_exists, mock_file):
        chain = load_memory_chain()
        self.assertEqual(chain, [])

    @patch("builtins.open", new_callable=mock_open, read_data='invalid_json')
    @patch("os.path.exists", return_value=True)
    def test_load_memory_chain_malformed_json(self, mock_exists, mock_file):
        chain = load_memory_chain()
        self.assertEqual(chain, [])

if __name__ == "__main__":
    unittest.main()

import unittest
import json
import os
from unittest.mock import patch, mock_open, MagicMock

from cognition.memory_bond_engine import (
    extract_symbols,
    build_bond_index,
    route_memory_by_symbol,
    save_bond_index
)

class TestMemoryBondEngine(unittest.TestCase):

    def test_extract_symbols_emotional(self):
        text = "I feel love and joy"
        symbols = extract_symbols(text)
        self.assertIn("emotion:love", symbols)
        self.assertIn("emotion:joy", symbols)

    def test_extract_symbols_numeric_and_concept(self):
        text = "We found 42 universes containing expansion"
        symbols = extract_symbols(text)
        self.assertIn("numeric", symbols)
        self.assertIn("concept:universes", symbols)
        self.assertIn("concept:expansion", symbols)

    def test_extract_symbols_timestamp(self):
        text = "tick 001"
        symbols = extract_symbols(text)
        self.assertIn("timestamp", symbols)

    def test_build_bond_index(self):
        mock_blocks = [
            {"uid": "m1", "content": "love expansion 001 tick 32"},
            {"uid": "m2", "content": "joy fear"}
        ]
        index = build_bond_index(mock_blocks)
        self.assertIn("emotion:love", index)
        self.assertIn("concept:expansion", index)
        self.assertIn("timestamp", index)
        self.assertIn("emotion:joy", index)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_and_route_memory(self, mock_file):
        test_index = {"emotion:love": ["m1"], "concept:truth": ["m2"]}
        save_bond_index(test_index)

        # Simulate file read
        mock_file().read.return_value = json.dumps(test_index)
        result = route_memory_by_symbol("concept:truth")
        self.assertEqual(result, ["m2"])

        result_empty = route_memory_by_symbol("nonexistent")
        self.assertEqual(result_empty, [])

if __name__ == "__main__":
    unittest.main()

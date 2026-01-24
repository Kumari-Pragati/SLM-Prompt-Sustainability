import unittest
from mbpp_299_code import defaultdict
from typing import List

from299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_aggregate([]))

    def test_single_entry(self):
        self.assertEqual(max_aggregate([("Alice", 85)]), ("Alice", 85))

    def test_multiple_entries_same_name(self):
        self.assertEqual(max_aggregate([("Alice", 85), ("Alice", 90)]), ("Alice", 90))

    def test_multiple_entries_different_names(self):
        self.assertEqual(max_aggregate([("Alice", 85), ("Bob", 90)]), ("Bob", 90))

    def test_negative_marks(self):
        self.assertEqual(max_aggregate([("Alice", -10), ("Bob", 90)]), ("Bob", 90))

    def test_zero_marks(self):
        self.assertEqual(max_aggregate([("Alice", 0), ("Bob", 90)]), ("Bob", 90))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_aggregate([(1, 85)])

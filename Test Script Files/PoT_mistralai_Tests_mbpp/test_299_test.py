import unittest
from mbpp_299_code import defaultdict
from 299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_aggregate([("Alice", 85), ("Bob", 75), ("Charlie", 90)]), ("Charlie", 90))
        self.assertEqual(max_aggregate([("Alice", 85), ("Bob", 75), ("Charlie", 90), ("Dave", 100)]), ("Dave", 100))

    def test_edge_case_empty(self):
        self.assertIsNone(max_aggregate([]))

    def test_edge_case_single_entry(self):
        self.assertEqual(max_aggregate([("Alice", 85)]), ("Alice", 85))

    def test_edge_case_duplicate_names(self):
        self.assertEqual(max_aggregate([("Alice", 85), ("Alice", 90)]), ("Alice", 90))

    def test_edge_case_negative_marks(self):
        self.assertEqual(max_aggregate([("Alice", -85), ("Bob", -75), ("Charlie", -90)]), ("Alice", -85))

    def test_corner_case_zero_marks(self):
        self.assertEqual(max_aggregate([("Alice", 0), ("Bob", 0), ("Charlie", 0)]), ("Alice", 0))

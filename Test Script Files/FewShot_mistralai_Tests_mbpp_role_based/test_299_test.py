import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):
    def test_positive_marks(self):
        self.assertEqual(max_aggregate([("Alice", 80), ("Bob", 75), ("Charlie", 90)]), ("Charlie", 90))
        self.assertEqual(max_aggregate([("Alice", 80), ("Bob", 75), ("Charlie", 90), ("Dave", 85)]), ("Charlie", 90))

    def test_zero_marks(self):
        self.assertEqual(max_aggregate([("Alice", 0), ("Bob", 0), ("Charlie", 0)]), ("Alice", 0))
        self.assertEqual(max_aggregate([("Alice", 0), ("Bob", 0), ("Charlie", 0), ("Dave", 0)]), ("Alice", 0))

    def test_negative_marks(self):
        self.assertEqual(max_aggregate([("Alice", -10), ("Bob", -5), ("Charlie", -20)]), ("Alice", -10))
        self.assertEqual(max_aggregate([("Alice", -10), ("Bob", -5), ("Charlie", -20), ("Dave", -15)]), ("Alice", -10))

    def test_empty_list(self):
        self.assertIsNone(max_aggregate([]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_aggregate(123)
        with self.assertRaises(TypeError):
            max_aggregate([(123, 45)])

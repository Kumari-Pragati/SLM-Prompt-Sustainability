import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):
    def test_largest_neg_typical(self):
        self.assertEqual(largest_neg([1, 2, 3, 4, 5]), 1)
        self.assertEqual(largest_neg([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(largest_neg([0, 0, 0, 0, 0]), 0)

    def test_largest_neg_empty(self):
        self.assertRaises(IndexError, largest_neg, [])

    def test_largest_neg_single_element(self):
        self.assertEqual(largest_neg([1]), 1)
        self.assertEqual(largest_neg([-1]), -1)
        self.assertEqual(largest_neg([0]), 0)

    def test_largest_neg_multiple_negative(self):
        self.assertEqual(largest_neg([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(largest_neg([-1, -2, -3, -4, -5, 0]), -5)

    def test_largest_neg_multiple_positive(self):
        self.assertEqual(largest_neg([1, 2, 3, 4, 5]), 1)
        self.assertEqual(largest_neg([1, 2, 3, 4, 5, 0]), 1)

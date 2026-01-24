import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):
    def test_positive_list(self):
        self.assertEqual(largest_neg([]), float('-inf'))
        self.assertEqual(largest_neg([1, 2, -3]), -3)
        self.assertEqual(largest_neg([-1, -2, -3]), -1)

    def test_empty_list(self):
        self.assertEqual(largest_neg([0]), 0)

    def test_single_element_list(self):
        self.assertEqual(largest_neg([-1]), -1)

    def test_negative_list(self):
        self.assertEqual(largest_neg([-1, -2, -3]), -3)

    def test_single_positive_element(self):
        self.assertEqual(largest_neg([1]), float('-inf'))

    def test_list_with_zero(self):
        self.assertEqual(largest_neg([0, -1]), -1)

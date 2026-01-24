import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_largest_neg_positive_list(self):
        self.assertEqual(largest_neg([1, 2, 3, 4, 5]), None)

    def test_largest_neg_empty_list(self):
        self.assertEqual(largest_neg([]), None)

    def test_largest_neg_single_element_list(self):
        self.assertEqual(largest_neg([1]), 1)

    def test_largest_neg_all_positive_list(self):
        self.assertEqual(largest_neg([1, 2, 3, 4, 5]), None)

    def test_largest_neg_all_negative_list(self):
        self.assertEqual(largest_neg([-5, -4, -3, -2, -1]), -5)

    def test_largest_neg_mixed_list(self):
        self.assertEqual(largest_neg([1, -2, 3, -4, 5]), -4)

import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(largest_neg([]), float('-inf'))

    def test_single_element_list(self):
        self.assertEqual(largest_neg([-1]), -1)

    def test_negative_numbers_list(self):
        self.assertEqual(largest_neg([-5, -2, 4, -1, -3, 0, -6]), -6)

    def test_positive_numbers_list(self):
        self.assertEqual(largest_neg([1, 2, 3, 4, 5]), float('-inf'))

    def test_mixed_numbers_list(self):
        self.assertEqual(largest_neg([-5, 2, -1, 4, 0, -3, 5]), -5)

    def test_float_numbers_list(self):
        self.assertEqual(largest_neg([-5.0, 2.0, -1.0, 4.0, 0.0, -3.0, 5.0]), -5.0)

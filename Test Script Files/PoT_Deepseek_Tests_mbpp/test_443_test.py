import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(largest_neg([-1, -2, -3, -4, -5]), -1)

    def test_single_negative_number(self):
        self.assertEqual(largest_neg([-5]), -5)

    def test_single_positive_number(self):
        self.assertEqual(largest_neg([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(largest_neg([]))

    def test_all_positive_numbers(self):
        self.assertIsNone(largest_neg([1, 2, 3, 4, 5]))

    def test_all_negative_numbers(self):
        self.assertEqual(largest_neg([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(largest_neg([-1, 2, -3, 4, -5]), -1)

    def test_duplicates(self):
        self.assertEqual(largest_neg([-1, -1, -2, -3, -4, -5]), -1)

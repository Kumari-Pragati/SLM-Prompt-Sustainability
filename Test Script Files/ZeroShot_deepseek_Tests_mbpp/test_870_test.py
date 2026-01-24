import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositiveNum(unittest.TestCase):

    def test_sum_positivenum_with_positive_numbers(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)

    def test_sum_positivenum_with_negative_numbers(self):
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5]), 0)

    def test_sum_positivenum_with_mixed_numbers(self):
        self.assertEqual(sum_positivenum([-1, 2, -3, 4, -5]), 6)

    def test_sum_positivenum_with_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_sum_positivenum_with_single_positive_number(self):
        self.assertEqual(sum_positivenum([5]), 5)

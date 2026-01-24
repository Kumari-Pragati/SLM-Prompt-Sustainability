import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositivenum(unittest.TestCase):
    def test_sum_positivenum_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_sum_positivenum_single_positive(self):
        self.assertEqual(sum_positivenum([1]), 1)

    def test_sum_positivenum_multiple_positive(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)

    def test_sum_positivenum_single_negative(self):
        self.assertEqual(sum_positivenum([-1]), 0)

    def test_sum_positivenum_multiple_positive_and_negative(self):
        self.assertEqual(sum_positivenum([1, 2, -3, 4, 5]), 8)

    def test_sum_positivenum_all_negative(self):
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5]), 0)

    def test_sum_positivenum_mixed_positive_and_zero(self):
        self.assertEqual(sum_positivenum([1, 0, 2, 3, 0]), 6)

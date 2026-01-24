import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativeNums(unittest.TestCase):

    def test_sum_negativenum_with_positive_numbers(self):
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5]), 0)

    def test_sum_negativenum_with_negative_numbers(self):
        self.assertEqual(sum_negativenum([-1, -2, -3, -4, -5]), -15)

    def test_sum_negativenum_with_mixed_numbers(self):
        self.assertEqual(sum_negativenum([-1, 2, -3, 4, -5]), -9)

    def test_sum_negativenum_with_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_sum_negativenum_with_single_negative_number(self):
        self.assertEqual(sum_negativenum([-1]), -1)

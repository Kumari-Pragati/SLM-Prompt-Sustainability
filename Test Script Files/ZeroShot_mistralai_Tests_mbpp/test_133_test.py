import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativeNum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_all_positive_numbers(self):
        self.assertEqual(sum_negativenum([1, 2, 3, 4]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(sum_negativenum([-1, -2, -3, -4]), -10)

    def test_mixed_numbers(self):
        self.assertEqual(sum_negativenum([-1, 1, -2, 3, -4, 2]), -3)

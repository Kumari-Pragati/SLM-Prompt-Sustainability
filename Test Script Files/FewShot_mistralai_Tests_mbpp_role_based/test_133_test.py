import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativeNum(unittest.TestCase):
    def test_sum_positive_numbers(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_sum_negative_numbers(self):
        self.assertEqual(sum_negativenum([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_single_negative_number(self):
        self.assertEqual(sum_negativenum([-1]), -1)

    def test_single_zero(self):
        self.assertEqual(sum_negativenum([0]), 0)

    def test_single_positive_number(self):
        self.assertEqual(sum_negativenum([1]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(sum_negativenum([-1, 0, 1, -2]), -3)

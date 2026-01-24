import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativeNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_negativenum([1, -2, 3, -4, 5]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_all_positive_numbers(self):
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(sum_negativenum([-1, -2, -3, -4, -5]), -15)

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(sum_negativenum([-1, 2, -3, 4, -5]), -3)

    def test_zero_in_list(self):
        self.assertEqual(sum_negativenum([0]), 0)

    def test_large_numbers(self):
        self.assertEqual(sum_negativenum([-1000000, 2000000, -3000000, 4000000, -5000000]), -15000000)

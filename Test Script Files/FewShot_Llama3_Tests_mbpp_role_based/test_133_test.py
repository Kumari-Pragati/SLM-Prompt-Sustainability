import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativenum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_single_negative_number(self):
        self.assertEqual(sum_negativenum([-1]), -1)

    def test_multiple_negative_numbers(self):
        self.assertEqual(sum_negativenum([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(sum_negativenum([1, -2, 3, -4]), -3)

    def test_all_negative_numbers(self):
        self.assertEqual(sum_negativenum([-1, -2, -3, -4, -5]), -15)

    def test_all_positive_numbers(self):
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5]), 0)

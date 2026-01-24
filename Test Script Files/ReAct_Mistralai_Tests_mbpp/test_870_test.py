import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositiveNum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_all_positive_numbers(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)

    def test_mixed_numbers(self):
        self.assertEqual(sum_positivenum([1, -2, 3, -4, 5]), 9)

    def test_zero_number(self):
        self.assertEqual(sum_positivenum([0, 1, 2, -3, 4]), 6)

    def test_large_numbers(self):
        self.assertEqual(sum_positivenum([1000000001, 1000000002, -1000000003]), 2000000001)

    def test_negative_numbers(self):
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5]), 0)

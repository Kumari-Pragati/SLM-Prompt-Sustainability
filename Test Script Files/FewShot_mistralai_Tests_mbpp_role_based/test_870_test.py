import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositivenum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)

    def test_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_positivenum([-1, -2, -3]), 0)

    def test_zero(self):
        self.assertEqual(sum_positivenum([0]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(sum_positivenum([1, -2, 3, -4, 5]), 9)

import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositivenum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(sum_positivenum([-1, -2, -3]), 0)

    def test_all_positive_numbers(self):
        self.assertEqual(sum_positivenum([1, 2, 3]), 6)

    def test_mixed_numbers(self):
        self.assertEqual(sum_positivenum([1, -2, 3, -4, 5]), 9)

    def test_large_numbers(self):
        self.assertEqual(sum_positivenum([1000000001, 1000000002, 1000000003]), 3000000006)

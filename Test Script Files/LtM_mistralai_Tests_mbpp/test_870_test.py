import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositivenum(unittest.TestCase):

    def test_simple_positive_list(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4]), 10)

    def test_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_positivenum([-1, -2, -3]), 0)

    def test_zero(self):
        self.assertEqual(sum_positivenum([0]), 0)

    def test_single_positive_number(self):
        self.assertEqual(sum_positivenum([5]), 5)

    def test_large_positive_numbers(self):
        self.assertEqual(sum_positivenum([1000000001, 2000000002, 3000000003]), 6000000006)

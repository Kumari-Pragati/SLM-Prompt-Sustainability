import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositiveNum(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertEqual(sum_positivenum([1, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(sum_positivenum([-1, -2, -3]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(sum_positivenum([-1, 2, 3]), 5)

    def test_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_single_positive_number(self):
        self.assertEqual(sum_positivenum([5]), 5)

    def test_single_negative_number(self):
        self.assertEqual(sum_positivenum([-5]), 0)

    def test_zero(self):
        self.assertEqual(sum_positivenum([0]), 0)

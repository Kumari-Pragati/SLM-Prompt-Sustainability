import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositiveNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)

    def test_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(sum_positivenum([-1, 2, -3, 4, -5]), 6)

    def test_single_positive_number(self):
        self.assertEqual(sum_positivenum([5]), 5)

    def test_single_negative_number(self):
        self.assertEqual(sum_positivenum([-5]), 0)

    def test_zero(self):
        self.assertEqual(sum_positivenum([0]), 0)

    def test_large_numbers(self):
        self.assertEqual(sum_positivenum([1000000, 2000000, 3000000]), 6000000)

import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):

    def test_sum_div_positive_numbers(self):
        self.assertEqual(sum_div(4), 3)
        self.assertEqual(sum_div(6), 3)
        self.assertEqual(sum_div(25), 4 + 5)
        self.assertEqual(sum_div(28), 4 + 7 + 14)
        self.assertEqual(sum_div(496), 4 + 8 + 12 + 16 + 31 + 64 + 96 + 128 + 169 + 232 + 256 + 336 + 384 + 448)

    def test_sum_div_zero(self):
        self.assertEqual(sum_div(0), 0)

    def test_sum_div_negative_numbers(self):
        self.assertEqual(sum_div(-4), -3)
        self.assertEqual(sum_div(-6), -3)
        self.assertEqual(sum_div(-25), -4 - 5)
        self.assertEqual(sum_div(-28), -4 - 7 - 14)
        self.assertEqual(sum_div(-496), -4 - 8 - 12 - 16 - 31 - 64 - 96 - 128 - 169 - 232 - 256 - 336 - 384 - 448)

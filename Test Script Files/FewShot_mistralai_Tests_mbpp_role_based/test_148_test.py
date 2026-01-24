import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_digits_twoparts(123), 12 + 3)
        self.assertEqual(sum_digits_twoparts(9876), 9 + 8 + 7 + 6)
        self.assertEqual(sum_digits_twoparts(10000), 1 + 0 + 0 + 0)

    def test_zero(self):
        self.assertEqual(sum_digits_twoparts(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_digits_twoparts(-123), -12 + 3)
        self.assertEqual(sum_digits_twoparts(-9876), -9 + 8 + 7 + 6)
        self.assertEqual(sum_digits_twoparts(-10000), -1 + 0 + 0 + 0)

    def test_large_numbers(self):
        self.assertEqual(sum_digits_twoparts(123456789), 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)
        self.assertEqual(sum_digits_twoparts(987654321), 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1)

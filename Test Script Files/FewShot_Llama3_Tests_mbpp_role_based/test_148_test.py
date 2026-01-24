import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_digits_twoparts(123), 6)
        self.assertEqual(sum_digits_twoparts(456), 15)
        self.assertEqual(sum_digits_twoparts(789), 24)

    def test_zero(self):
        self.assertEqual(sum_digits_twoparts(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_digits_twoparts(-123), 6)
        self.assertEqual(sum_digits_twoparts(-456), 15)
        self.assertEqual(sum_digits_twoparts(-789), 24)

    def test_large_numbers(self):
        self.assertEqual(sum_digits_twoparts(123456789), 81)
        self.assertEqual(sum_digits_twoparts(987654321), 81)

    def test_edge_cases(self):
        self.assertEqual(sum_digits_twoparts(1000000000), 27)
        self.assertEqual(sum_digits_twoparts(999999999), 27)

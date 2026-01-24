import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(sum_digits_twoparts(123), 6)
        self.assertEqual(sum_digits_twoparts(987), 14)
        self.assertEqual(sum_digits_twoparts(1024), 6)
        self.assertEqual(sum_digits_twoparts(12345), 15)

    def test_edge_cases(self):
        self.assertEqual(sum_digits_twoparts(0), 0)
        self.assertEqual(sum_digits_twoparts(9), 9)
        self.assertEqual(sum_digits_twoparts(10), 1)
        self.assertEqual(sum_digits_twoparts(99), 18)
        self.assertEqual(sum_digits_twoparts(100), 1)

    def test_corner_cases(self):
        self.assertEqual(sum_digits_twoparts(1000), 1)
        self.assertEqual(sum_digits_twoparts(10000), 1 + 9 + 18 + 27)
        self.assertEqual(sum_digits_twoparts(100000), 1 + 9 + 18 + 27 + 36 + 45)

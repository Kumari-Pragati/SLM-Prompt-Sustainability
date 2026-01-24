import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(sum_digits_twoparts(1234), 12 + 34)
        self.assertEqual(sum_digits_twoparts(9876), 9 + 8 + 7 + 6)
        self.assertEqual(sum_digits_twoparts(10), 1 + 0)

    def test_edge_cases(self):
        self.assertEqual(sum_digits_twoparts(0), 0)
        self.assertEqual(sum_digits_twoparts(1), 1)
        self.assertEqual(sum_digits_twoparts(99), 9 + 9)
        self.assertEqual(sum_digits_twoparts(100), 1)

    def test_boundary_cases(self):
        self.assertEqual(sum_digits_twoparts(1000), 1 + 0 + 0)
        self.assertEqual(sum_digits_twoparts(9999), 9 + 9 + 9 + 9)
        self.assertEqual(sum_digits_twoparts(999_999), 9 + 9 + 9 + 9_998)

    def test_negative_input(self):
        self.assertEqual(sum_digits_twoparts(-1234), -(12 + 34))
        self.assertEqual(sum_digits_twoparts(-9876), -(9 + 8 + 7 + 6))

import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):

    def test_sum_digits_twoparts(self):
        self.assertEqual(sum_digits_twoparts(10), 1)
        self.assertEqual(sum_digits_twoparts(123), 6)
        self.assertEqual(sum_digits_twoparts(456), 15)
        self.assertEqual(sum_digits_twoparts(789), 24)
        self.assertEqual(sum_digits_twoparts(1000), 1)
        self.assertEqual(sum_digits_twoparts(123456), 21)
        self.assertEqual(sum_digits_twoparts(123456789), 45)

    def test_sum_digits_twoparts_edge_cases(self):
        self.assertEqual(sum_digits_twoparts(0), 0)
        self.assertEqual(sum_digits_twoparts(9), 9)
        self.assertEqual(sum_digits_twoparts(99), 18)
        self.assertEqual(sum_digits_twoparts(999), 27)
        self.assertEqual(sum_digits_twoparts(9999), 36)

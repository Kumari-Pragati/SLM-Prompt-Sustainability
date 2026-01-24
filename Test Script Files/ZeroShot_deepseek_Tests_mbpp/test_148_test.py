import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):

    def test_sum_digits_single(self):
        self.assertEqual(sum_digits_single(123), 6)
        self.assertEqual(sum_digits_single(999), 27)
        self.assertEqual(sum_digits_single(0), 0)

    def test_closest(self):
        self.assertEqual(closest(123), 99)
        self.assertEqual(closest(999), 999)
        self.assertEqual(closest(0), 0)

    def test_sum_digits_twoparts(self):
        self.assertEqual(sum_digits_twoparts(123), 18)
        self.assertEqual(sum_digits_twoparts(999), 27)
        self.assertEqual(sum_digits_twoparts(0), 0)

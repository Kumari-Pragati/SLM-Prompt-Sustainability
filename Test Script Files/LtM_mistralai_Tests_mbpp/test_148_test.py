import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(sum_digits_twoparts(12), 3)
        self.assertEqual(sum_digits_twoparts(99), 18)
        self.assertEqual(sum_digits_twoparts(100), 1)

    def test_edge_cases(self):
        self.assertEqual(sum_digits_twoparts(0), 0)
        self.assertEqual(sum_digits_twoparts(1), 1)
        self.assertEqual(sum_digits_twoparts(9), 9)
        self.assertEqual(sum_digits_twoparts(10), 1)
        self.assertEqual(sum_digits_twoparts(999), 91)
        self.assertEqual(sum_digits_twoparts(1000), 1)

    def test_complex(self):
        self.assertEqual(sum_digits_twoparts(10000), 101)
        self.assertEqual(sum_digits_twoparts(100000), 10101)
        self.assertEqual(sum_digits_twoparts(1000000), 1010101)
        self.assertEqual(sum_digits_twoparts(10000000), 101010101)

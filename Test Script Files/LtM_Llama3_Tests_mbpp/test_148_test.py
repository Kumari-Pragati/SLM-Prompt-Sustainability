import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_digits_twoparts(10), 1)
        self.assertEqual(sum_digits_twoparts(20), 2)
        self.assertEqual(sum_digits_twoparts(30), 3)
        self.assertEqual(sum_digits_twoparts(40), 4)
        self.assertEqual(sum_digits_twoparts(50), 5)

    def test_edge(self):
        self.assertEqual(sum_digits_twoparts(0), 0)
        self.assertEqual(sum_digits_twoparts(9), 9)
        self.assertEqual(sum_digits_twoparts(99), 18)
        self.assertEqual(sum_digits_twoparts(100), 1)
        self.assertEqual(sum_digits_twoparts(101), 2)

    def test_complex(self):
        self.assertEqual(sum_digits_twoparts(123), 6)
        self.assertEqual(sum_digits_twoparts(456), 15)
        self.assertEqual(sum_digits_twoparts(789), 24)
        self.assertEqual(sum_digits_twoparts(1000), 1)
        self.assertEqual(sum_digits_twoparts(1234), 10)

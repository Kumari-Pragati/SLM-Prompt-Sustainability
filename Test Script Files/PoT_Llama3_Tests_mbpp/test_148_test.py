import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(sum_digits_twoparts(123), 6)
        self.assertEqual(sum_digits_twoparts(456), 15)
        self.assertEqual(sum_digits_twoparts(789), 24)

    def test_edge(self):
        self.assertEqual(sum_digits_twoparts(0), 0)
        self.assertEqual(sum_digits_twoparts(9), 9)
        self.assertEqual(sum_digits_twoparts(99), 18)
        self.assertEqual(sum_digits_twoparts(100), 1)

    def test_boundary(self):
        self.assertEqual(sum_digits_twoparts(101), 2)
        self.assertEqual(sum_digits_twoparts(111), 6)
        self.assertEqual(sum_digits_twoparts(1234), 10)
        self.assertEqual(sum_digits_twoparts(12345), 15)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            sum_digits_twoparts('abc')
        with self.assertRaises(TypeError):
            sum_digits_twoparts(None)

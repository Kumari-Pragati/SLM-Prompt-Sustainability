import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):
    def test_sum_digits_twoparts(self):
        self.assertEqual(sum_digits_twoparts(10), 1)
        self.assertEqual(sum_digits_twoparts(123), 6)
        self.assertEqual(sum_digits_twoparts(999), 27)
        self.assertEqual(sum_digits_twoparts(1000), 1)
        self.assertEqual(sum_digits_twoparts(123456789), 45)
        self.assertEqual(sum_digits_twoparts(0), 0)
        self.assertEqual(sum_digits_twoparts(1), 1)
        self.assertEqual(sum_digits_twoparts(9), 9)
        self.assertEqual(sum_digits_twoparts(10**9), 9)

    def test_edge_cases(self):
        self.assertEqual(sum_digits_twoparts(-10), 1)
        self.assertEqual(sum_digits_twoparts(-123), 6)
        self.assertEqual(sum_digits_twoparts(-999), 27)
        self.assertEqual(sum_digits_twoparts(-1000), 1)
        self.assertEqual(sum_digits_twoparts(-123456789), 45)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_digits_twoparts('abc')
        with self.assertRaises(TypeError):
            sum_digits_twoparts(None)
        with self.assertRaises(TypeError):
            sum_digits_twoparts([1, 2, 3])

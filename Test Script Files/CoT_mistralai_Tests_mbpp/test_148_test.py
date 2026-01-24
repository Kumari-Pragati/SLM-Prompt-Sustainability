import unittest
from148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_digits_twoparts(123), 12 + 3)
        self.assertEqual(sum_digits_twoparts(987), 9 + 8 + 7)
        self.assertEqual(sum_digits_twoparts(1024), 1 + 2 + 4)

    def test_zero(self):
        self.assertEqual(sum_digits_twoparts(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_digits_twoparts(-123), -12 + 3)
        self.assertEqual(sum_digits_twoparts(-987), -9 + 8 + 7)
        self.assertEqual(sum_digits_twoparts(-1024), -1 + 2 + 4)

    def test_edge_cases(self):
        self.assertEqual(sum_digits_twoparts(9), 9)
        self.assertEqual(sum_digits_twoparts(10), 1)
        self.assertEqual(sum_digits_twoparts(19), 1 + 9)
        self.assertEqual(sum_digits_twoparts(99), 9 + 9)
        self.assertEqual(sum_digits_twoparts(199), 1 + 9 + 9)

    def test_large_numbers(self):
        self.assertEqual(sum_digits_twoparts(123456789), 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)
        self.assertEqual(sum_digits_twoparts(987654321), 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, sum_digits_twoparts, "string")
        self.assertRaises(TypeError, sum_digits_twoparts, 0.123)
        self.assertRaises(TypeError, sum_digits_twoparts, [1, 2, 3])

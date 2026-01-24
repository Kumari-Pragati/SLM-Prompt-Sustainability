import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(sum_digits_twoparts(1), 1)

    def test_two_digits(self):
        self.assertEqual(sum_digits_twoparts(12), 3)

    def test_three_digits(self):
        self.assertEqual(sum_digits_twoparts(123), 6)

    def test_four_digits(self):
        self.assertEqual(sum_digits_twoparts(1234), 10)

    def test_five_digits(self):
        self.assertEqual(sum_digits_twoparts(12345), 15)

    def test_edge_case_zero(self):
        self.assertEqual(sum_digits_twoparts(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            sum_digits_twoparts(-123)

    def test_edge_case_large(self):
        self.assertEqual(sum_digits_twoparts(123456789), 45)

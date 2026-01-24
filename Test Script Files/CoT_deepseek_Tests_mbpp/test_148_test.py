import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_digits_twoparts(12345), 15)

    def test_single_digit_number(self):
        self.assertEqual(sum_digits_twoparts(9), 9)

    def test_large_number(self):
        self.assertEqual(sum_digits_twoparts(123456789), 45)

    def test_boundary_case_zero(self):
        self.assertEqual(sum_digits_twoparts(0), 0)

    def test_boundary_case_single_digit_above_9(self):
        self.assertEqual(sum_digits_twoparts(10), 1)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            sum_digits_twoparts(-12345)

    def test_non_integer_input(self):
        with self.assertRaises(Exception):
            sum_digits_twoparts(12345.6)

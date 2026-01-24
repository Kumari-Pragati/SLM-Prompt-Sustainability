import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):

    def test_simple_decimal(self):
        self.assertTrue(is_decimal('123.45'))

    def test_integer(self):
        self.assertTrue(is_decimal('123'))

    def test_decimal_with_one_digit_after_point(self):
        self.assertTrue(is_decimal('123.4'))

    def test_decimal_with_two_digits_after_point(self):
        self.assertTrue(is_decimal('123.45'))

    def test_decimal_with_more_than_two_digits_after_point(self):
        self.assertFalse(is_decimal('123.456'))

    def test_empty_string(self):
        self.assertFalse(is_decimal(''))

    def test_decimal_with_leading_zero(self):
        self.assertFalse(is_decimal('0123.45'))

    def test_decimal_with_trailing_zero(self):
        self.assertTrue(is_decimal('123.0'))

    def test_decimal_with_extra_zeroes(self):
        self.assertTrue(is_decimal('123.00'))

    def test_decimal_with_negative_value(self):
        self.assertFalse(is_decimal('-123.45'))

    def test_decimal_with_alphabetic_characters(self):
        self.assertFalse(is_decimal('123abc'))

    def test_decimal_with_special_characters(self):
        self.assertFalse(is_decimal('123@45'))

import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):

    def test_simple_decimal(self):
        self.assertTrue(is_decimal('123.45'))

    def test_integer(self):
        self.assertTrue(is_decimal('123'))

    def test_decimal_without_fractional_part(self):
        self.assertTrue(is_decimal('123.'))

    def test_decimal_with_single_digit_fractional_part(self):
        self.assertTrue(is_decimal('123.4'))

    def test_decimal_with_two_digits_fractional_part(self):
        self.assertTrue(is_decimal('123.45'))

    def test_decimal_with_more_than_two_digits_fractional_part(self):
        self.assertFalse(is_decimal('123.456'))

    def test_empty_string(self):
        self.assertFalse(is_decimal(''))

    def test_decimal_with_leading_zero(self):
        self.assertFalse(is_decimal('0123.45'))

    def test_decimal_with_trailing_zero(self):
        self.assertFalse(is_decimal('123.450'))

    def test_decimal_with_extra_decimal_point(self):
        self.assertFalse(is_decimal('123.45.67'))

    def test_decimal_with_negative_value(self):
        self.assertFalse(is_decimal('-123.45'))

    def test_decimal_with_alphabetic_characters(self):
        self.assertFalse(is_decimal('123abc'))

    def test_decimal_with_special_characters(self):
        self.assertFalse(is_decimal('123@45'))

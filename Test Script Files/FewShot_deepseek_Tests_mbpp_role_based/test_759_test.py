import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_typical_decimal(self):
        self.assertTrue(is_decimal('123.45'))

    def test_integer(self):
        self.assertTrue(is_decimal('123'))

    def test_decimal_with_two_digits(self):
        self.assertTrue(is_decimal('123.45'))

    def test_decimal_with_one_digit(self):
        self.assertTrue(is_decimal('123.4'))

    def test_decimal_without_fractional_part(self):
        self.assertTrue(is_decimal('123.'))

    def test_decimal_with_leading_zero(self):
        self.assertFalse(is_decimal('0123.45'))

    def test_decimal_with_trailing_zero(self):
        self.assertTrue(is_decimal('123.450'))

    def test_decimal_with_more_than_two_fractional_digits(self):
        self.assertFalse(is_decimal('123.456'))

    def test_negative_decimal(self):
        self.assertFalse(is_decimal('-123.45'))

    def test_empty_string(self):
        self.assertFalse(is_decimal(''))

    def test_non_decimal_string(self):
        self.assertFalse(is_decimal('abc'))

    def test_decimal_with_space(self):
        self.assertFalse(is_decimal('123.45 '))

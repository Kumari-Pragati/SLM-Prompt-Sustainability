import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_positive_integer(self):
        self.assertTrue(is_decimal('123'))

    def test_positive_float(self):
        self.assertTrue(is_decimal('123.45'))

    def test_negative_integer(self):
        self.assertFalse(is_decimal('-123'))

    def test_negative_float(self):
        self.assertFalse(is_decimal('-123.45'))

    def test_zero(self):
        self.assertTrue(is_decimal('0'))

    def test_empty_string(self):
        self.assertFalse(is_decimal(''))

    def test_non_numeric_string(self):
        self.assertFalse(is_decimal('abc'))

    def test_decimal_with_trailing_zeros(self):
        self.assertTrue(is_decimal('123.00'))

    def test_decimal_with_leading_zeros(self):
        self.assertTrue(is_decimal('0123.45'))

    def test_decimal_with_leading_and_trailing_zeros(self):
        self.assertTrue(is_decimal('0123.00'))

    def test_decimal_with_leading_zeros_and_trailing_zeros(self):
        self.assertTrue(is_decimal('0123.00'))

    def test_decimal_with_leading_zeros_and_trailing_zeros_and_trailing_zeros(self):
        self.assertTrue(is_decimal('0123.000'))

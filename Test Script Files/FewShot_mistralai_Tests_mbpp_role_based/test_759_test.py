import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_positive_decimal(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('123.0'))

    def test_zero_decimal(self):
        self.assertTrue(is_decimal('0'))
        self.assertTrue(is_decimal('0.0'))

    def test_negative_decimal(self):
        self.assertTrue(is_decimal('-123'))
        self.assertTrue(is_decimal('-123.45'))
        self.assertTrue(is_decimal('-123.0'))

    def test_empty_string(self):
        self.assertFalse(is_decimal(''))

    def test_whitespace(self):
        self.assertFalse(is_decimal('  123'))
        self.assertFalse(is_decimal('  123.45'))
        self.assertFalse(is_decimal('  123.0'))

    def test_leading_zero(self):
        self.assertTrue(is_decimal('0123'))
        self.assertTrue(is_decimal('0123.45'))
        self.assertTrue(is_decimal('0123.0'))

    def test_trailing_zero(self):
        self.assertTrue(is_decimal('1230'))
        self.assertTrue(is_decimal('123.450'))
        self.assertTrue(is_decimal('123.00'))

    def test_long_number(self):
        self.assertTrue(is_decimal('12345678901234567890.123456'))

    def test_max_decimal_places(self):
        self.assertTrue(is_decimal('123.45'))
        self.assertFalse(is_decimal('123.456'))

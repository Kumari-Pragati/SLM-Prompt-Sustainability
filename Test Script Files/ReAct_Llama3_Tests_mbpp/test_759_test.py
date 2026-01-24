import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):

    def test_positive_integer(self):
        self.assertTrue(is_decimal('123'))

    def test_positive_float(self):
        self.assertTrue(is_decimal('123.45'))

    def test_negative_integer(self):
        self.assertTrue(is_decimal('-123'))

    def test_negative_float(self):
        self.assertTrue(is_decimal('-123.45'))

    def test_zero(self):
        self.assertTrue(is_decimal('0'))

    def test_empty_string(self):
        self.assertFalse(is_decimal(''))

    def test_non_numeric_string(self):
        self.assertFalse(is_decimal('abc'))

    def test_non_numeric_string_with_decimal(self):
        self.assertFalse(is_decimal('abc.123'))

    def test_non_numeric_string_with_multiple_decimals(self):
        self.assertFalse(is_decimal('abc.123.456'))

    def test_non_numeric_string_with_leading_decimal(self):
        self.assertFalse(is_decimal('.123'))

    def test_non_numeric_string_with_trailing_decimal(self):
        self.assertFalse(is_decimal('123.'))

    def test_non_numeric_string_with_multiple_leading_decimals(self):
        self.assertFalse(is_decimal('..123'))

    def test_non_numeric_string_with_multiple_trailing_decimals(self):
        self.assertFalse(is_decimal('123..'))

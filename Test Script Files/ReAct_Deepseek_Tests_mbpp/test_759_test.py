import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('0.0'))
        self.assertTrue(is_decimal('123'))

    def test_edge_cases(self):
        self.assertFalse(is_decimal('123.456'))  # More than 2 decimal places
        self.assertFalse(is_decimal('123.'))     # Decimal point without a digit after it
        self.assertFalse(is_decimal('.'))        # Only a decimal point
        self.assertFalse(is_decimal(''))         # Empty string

    def test_explicitly_handled_error_cases(self):
        self.assertFalse(is_decimal('123.a'))   # Non-numeric character after decimal point
        self.assertFalse(is_decimal('123.!'))   # Non-numeric character after decimal point
        self.assertFalse(is_decimal('123. '))   # Trailing space after decimal point

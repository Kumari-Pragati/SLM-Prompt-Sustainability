import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):

    def test_is_decimal_positive(self):
        self.assertTrue(is_decimal("123"))
        self.assertTrue(is_decimal("123.45"))
        self.assertTrue(is_decimal("123.0"))
        self.assertTrue(is_decimal("0"))
        self.assertTrue(is_decimal("0.123"))

    def test_is_decimal_negative(self):
        self.assertFalse(is_decimal("abc"))
        self.assertFalse(is_decimal("123a"))
        self.assertFalse(is_decimal("123z"))
        self.assertFalse(is_decimal("123!@#"))
        self.assertFalse(is_decimal("123.45678"))  # more than 2 decimal places
        self.assertFalse(is_decimal("123e4"))  # exponential notation
        self.assertFalse(is_decimal("123-"))  # negative number with a minus sign

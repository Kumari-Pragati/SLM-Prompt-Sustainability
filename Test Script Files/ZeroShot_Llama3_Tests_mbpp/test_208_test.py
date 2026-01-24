import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):

    def test_positive_decimal(self):
        self.assertTrue(is_decimal("123"))
        self.assertTrue(is_decimal("123.45"))
        self.assertTrue(is_decimal("123."))
        self.assertTrue(is_decimal("123."))

    def test_negative_decimal(self):
        self.assertTrue(is_decimal("-123"))
        self.assertTrue(is_decimal("-123.45"))
        self.assertTrue(is_decimal("-123."))
        self.assertTrue(is_decimal("-123."))

    def test_zero(self):
        self.assertTrue(is_decimal("0"))
        self.assertTrue(is_decimal("0."))
        self.assertTrue(is_decimal(".0"))

    def test_non_decimal(self):
        self.assertFalse(is_decimal("123abc"))
        self.assertFalse(is_decimal("123.abc"))
        self.assertFalse(is_decimal("abc123"))
        self.assertFalse(is_decimal("abc.123"))

    def test_empty_string(self):
        self.assertFalse(is_decimal(""))

    def test_non_numeric(self):
        self.assertFalse(is_decimal("abc"))
        self.assertFalse(is_decimal("abc."))
        self.assertFalse(is_decimal(".abc"))

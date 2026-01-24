import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):

    def test_positive_integer(self):
        self.assertTrue(is_decimal(123))

    def test_zero(self):
        self.assertTrue(is_decimal(0))

    def test_negative_integer(self):
        self.assertTrue(is_decimal(-456))

    def test_single_decimal_place(self):
        self.assertTrue(is_decimal(123.4))

    def test_double_decimal_place(self):
        self.assertTrue(is_decimal(123.45))

    def test_no_decimal_place(self):
        self.assertTrue(is_decimal(123))

    def test_empty_string(self):
        self.assertFalse(is_decimal(""))

    def test_whitespace_only(self):
        self.assertFalse(is_decimal("   "))

    def test_leading_whitespace(self):
        self.assertFalse(is_decimal(" 123"))

    def test_trailing_whitespace(self):
        self.assertFalse(is_decimal("123 "))

    def test_leading_and_trailing_whitespace(self):
        self.assertFalse(is_decimal(" 123 "))

    def test_non_numeric_characters(self):
        self.assertFalse(is_decimal("123a"))
        self.assertFalse(is_decimal("123z"))
        self.assertFalse(is_decimal("123!"))

    def test_long_number(self):
        self.assertTrue(is_decimal(12345678901234567890))

    def test_long_number_with_decimal(self):
        self.assertTrue(is_decimal(1234567890.1234567890))

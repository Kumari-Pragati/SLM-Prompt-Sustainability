import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_valid_decimal(self):
        self.assertTrue(is_decimal("12.34"))

    def test_valid_integer(self):
        self.assertTrue(is_decimal("123"))

    def test_valid_decimal_with_trailing_zeros(self):
        self.assertTrue(is_decimal("12.00"))

    def test_invalid_non_numeric_input(self):
        self.assertFalse(is_decimal("abc"))

    def test_invalid_non_decimal_input(self):
        self.assertFalse(is_decimal("12.3456"))

    def test_empty_input(self):
        self.assertFalse(is_decimal(""))

    def test_single_digit_input(self):
        self.assertTrue(is_decimal("1"))

    def test_two_digit_input(self):
        self.assertTrue(is_decimal("12"))

    def test_max_decimal_places(self):
        self.assertTrue(is_decimal("123.99"))

    def test_max_integer_value(self):
        self.assertTrue(is_decimal("99999999999999999999"))

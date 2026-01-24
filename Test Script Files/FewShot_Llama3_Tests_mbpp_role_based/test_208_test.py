import unittest
from mbpp_208_code import is_decimal

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
        self.assertFalse(is_decimal("123abc"))

    def test_empty_input(self):
        self.assertFalse(is_decimal(""))

    def test_single_digit_input(self):
        self.assertTrue(is_decimal("1"))

    def test_two_digit_input(self):
        self.assertTrue(is_decimal("12"))

    def test_max_two_decimal_places_input(self):
        self.assertTrue(is_decimal("123.45"))

    def test_max_two_decimal_places_input_with_trailing_zeros(self):
        self.assertTrue(is_decimal("123.45"))

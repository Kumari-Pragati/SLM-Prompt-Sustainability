import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_positive_decimal(self):
        self.assertTrue(is_decimal("12.34"))

    def test_negative_decimal(self):
        self.assertTrue(is_decimal("-12.34"))

    def test_zero(self):
        self.assertTrue(is_decimal("0"))

    def test_whole_number(self):
        self.assertTrue(is_decimal("123"))

    def test_decimal_with_two_places(self):
        self.assertTrue(is_decimal("123.45"))

    def test_decimal_with_more_than_two_places(self):
        self.assertFalse(is_decimal("123.456"))

    def test_decimal_without_any_digits(self):
        self.assertFalse(is_decimal("."))

    def test_decimal_without_fractional_part(self):
        self.assertTrue(is_decimal("123."))

    def test_empty_string(self):
        self.assertFalse(is_decimal(""))

    def test_non_decimal_string(self):
        self.assertFalse(is_decimal("abc"))

    def test_decimal_with_leading_zero(self):
        self.assertFalse(is_decimal("012.34"))

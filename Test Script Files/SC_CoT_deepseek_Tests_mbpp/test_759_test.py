import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):

    def test_typical_decimal(self):
        self.assertTrue(is_decimal('123.45'))

    def test_integer(self):
        self.assertTrue(is_decimal('123'))

    def test_decimal_without_fractional_part(self):
        self.assertTrue(is_decimal('123.'))

    def test_decimal_with_single_digit_fractional_part(self):
        self.assertTrue(is_decimal('123.4'))

    def test_decimal_with_two_digits_fractional_part(self):
        self.assertTrue(is_decimal('123.45'))

    def test_decimal_with_more_than_two_digits_fractional_part(self):
        self.assertFalse(is_decimal('123.456'))

    def test_negative_decimal(self):
        self.assertTrue(is_decimal('-123.45'))

    def test_negative_decimal_without_fractional_part(self):
        self.assertTrue(is_decimal('-123.'))

    def test_negative_decimal_with_single_digit_fractional_part(self):
        self.assertTrue(is_decimal('-123.4'))

    def test_negative_decimal_with_two_digits_fractional_part(self):
        self.assertTrue(is_decimal('-123.45'))

    def test_negative_decimal_with_more_than_two_digits_fractional_part(self):
        self.assertFalse(is_decimal('-123.456'))

    def test_empty_string(self):
        self.assertFalse(is_decimal(''))

    def test_invalid_characters(self):
        self.assertFalse(is_decimal('123abc'))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            is_decimal(123)

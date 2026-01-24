import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):

    def test_typical_decimal(self):
        self.assertTrue(is_decimal('123.45'))

    def test_integer(self):
        self.assertTrue(is_decimal('123'))

    def test_decimal_with_one_digit_after_point(self):
        self.assertTrue(is_decimal('123.1'))

    def test_decimal_with_two_digits_after_point(self):
        self.assertTrue(is_decimal('123.45'))

    def test_decimal_with_more_than_two_digits_after_point(self):
        self.assertFalse(is_decimal('123.456'))

    def test_negative_decimal(self):
        self.assertTrue(is_decimal('-123.45'))

    def test_negative_integer(self):
        self.assertTrue(is_decimal('-123'))

    def test_negative_decimal_with_one_digit_after_point(self):
        self.assertTrue(is_decimal('-123.1'))

    def test_negative_decimal_with_two_digits_after_point(self):
        self.assertTrue(is_decimal('-123.45'))

    def test_negative_decimal_with_more_than_two_digits_after_point(self):
        self.assertFalse(is_decimal('-123.456'))

    def test_empty_string(self):
        self.assertFalse(is_decimal(''))

    def test_non_decimal_string(self):
        self.assertFalse(is_decimal('abc'))

    def test_decimal_with_non_digit_characters(self):
        self.assertFalse(is_decimal('123.abc'))

    def test_decimal_with_extra_spaces(self):
        self.assertFalse(is_decimal(' 123.45 '))

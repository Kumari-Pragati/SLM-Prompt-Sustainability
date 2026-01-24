import unittest
from mbpp_759_code import is_decimal

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

    def test_decimal_with_no_digits_after_point(self):
        self.assertFalse(is_decimal('123.'))

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

    def test_negative_decimal_with_no_digits_after_point(self):
        self.assertFalse(is_decimal('-123.'))

    def test_invalid_input(self):
        self.assertFalse(is_decimal('123.456.789'))

    def test_empty_string(self):
        self.assertFalse(is_decimal(''))

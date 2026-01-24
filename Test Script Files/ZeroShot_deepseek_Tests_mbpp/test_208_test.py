import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):

    def test_positive_decimal(self):
        self.assertTrue(is_decimal('12.34'))

    def test_negative_decimal(self):
        self.assertTrue(is_decimal('-12.34'))

    def test_positive_integer(self):
        self.assertTrue(is_decimal('12'))

    def test_negative_integer(self):
        self.assertTrue(is_decimal('-12'))

    def test_decimal_with_more_than_two_decimal_places(self):
        self.assertFalse(is_decimal('12.345'))

    def test_decimal_without_decimal_part(self):
        self.assertTrue(is_decimal('12.'))

    def test_decimal_with_only_zero_after_decimal(self):
        self.assertTrue(is_decimal('12.0'))

    def test_non_decimal_string(self):
        self.assertFalse(is_decimal('12a'))

    def test_empty_string(self):
        self.assertFalse(is_decimal(''))

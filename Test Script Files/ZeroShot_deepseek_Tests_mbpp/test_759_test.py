import unittest
from mbpp_759_code import is_decimal

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

    def test_decimal_with_leading_zeroes(self):
        self.assertFalse(is_decimal('0012.34'))

    def test_non_decimal_string(self):
        self.assertFalse(is_decimal('12abc'))

    def test_empty_string(self):
        self.assertFalse(is_decimal(''))

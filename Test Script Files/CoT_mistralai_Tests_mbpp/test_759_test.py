import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('123.0'))
        self.assertTrue(is_decimal('0'))
        self.assertTrue(is_decimal('0.1'))

    def test_negative(self):
        self.assertFalse(is_decimal('abc'))
        self.assertFalse(is_decimal('123a'))
        self.assertFalse(is_decimal('123z'))
        self.assertFalse(is_decimal('123!'))
        self.assertFalse(is_decimal('-123'))
        self.assertFalse(is_decimal('-123.45'))
        self.assertFalse(is_decimal('-123.0'))
        self.assertFalse(is_decimal('-0'))
        self.assertFalse(is_decimal('-.1'))

    def test_edge_cases(self):
        self.assertTrue(is_decimal('12345678901234567890.12'))
        self.assertTrue(is_decimal('12345678901234567890.0'))
        self.assertFalse(is_decimal('123456789012345678901234567890.123'))
        self.assertFalse(is_decimal('123456789012345678901234567890'))
        self.assertTrue(is_decimal('0.0'))
        self.assertTrue(is_decimal('0.12345678901234567890'))

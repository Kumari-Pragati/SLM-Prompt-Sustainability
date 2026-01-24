import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_valid_decimal(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('123.0'))

    def test_empty_string(self):
        self.assertFalse(is_decimal(''))

    def test_non_decimal(self):
        self.assertFalse(is_decimal('abc'))
        self.assertFalse(is_decimal('123a'))
        self.assertFalse(is_decimal('-123'))
        self.assertFalse(is_decimal('+123'))

    def test_long_decimal(self):
        self.assertTrue(is_decimal('1234567890.1234'))

    def test_short_decimal(self):
        self.assertTrue(is_decimal('0.1'))
        self.assertTrue(is_decimal('0'))

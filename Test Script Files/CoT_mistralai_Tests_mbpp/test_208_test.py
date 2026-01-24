import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('123.0'))

    def test_negative(self):
        self.assertFalse(is_decimal('123a'))
        self.assertFalse(is_decimal('123z'))
        self.assertFalse(is_decimal('123!'))
        self.assertFalse(is_decimal('123-'))
        self.assertFalse(is_decimal('123.'))
        self.assertFalse(is_decimal('123e4'))
        self.assertFalse(is_decimal('-123'))
        self.assertFalse(is_decimal('-123.'))
        self.assertFalse(is_decimal('+123'))
        self.assertFalse(is_decimal('+123.'))

    def test_edge_cases(self):
        self.assertTrue(is_decimal('1'))
        self.assertTrue(is_decimal('0'))
        self.assertTrue(is_decimal('1234567890'))
        self.assertTrue(is_decimal('123.00'))
        self.assertFalse(is_decimal('123.123'))
        self.assertFalse(is_decimal('1234567890.123'))
        self.assertFalse(is_decimal('1234567890123'))
        self.assertFalse(is_decimal('.'))
        self.assertFalse(is_decimal('-.'))
        self.assertFalse(is_decimal('+.'))

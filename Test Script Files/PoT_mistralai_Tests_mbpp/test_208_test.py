import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_typical_decimal(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('0'))
        self.assertTrue(is_decimal('123.0'))

    def test_edge_cases(self):
        self.assertFalse(is_decimal('123abc'))
        self.assertFalse(is_decimal('-123'))
        self.assertFalse(is_decimal('+123'))
        self.assertTrue(is_decimal('123e4'))
        self.assertTrue(is_decimal('123e-4'))
        self.assertFalse(is_decimal('123e-5'))
        self.assertFalse(is_decimal('123e+5'))
        self.assertTrue(is_decimal('123.000'))
        self.assertFalse(is_decimal('123.0000'))
        self.assertFalse(is_decimal('123.123456789'))

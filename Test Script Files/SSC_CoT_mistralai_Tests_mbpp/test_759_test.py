import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_normal_input(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('123.0'))

    def test_edge_input(self):
        self.assertTrue(is_decimal('1234567890'))
        self.assertTrue(is_decimal('123.456'))
        self.assertFalse(is_decimal('123.456789'))
        self.assertTrue(is_decimal('123.00'))
        self.assertFalse(is_decimal('123.000'))

    def test_corner_input(self):
        self.assertTrue(is_decimal('0'))
        self.assertTrue(is_decimal('-123'))
        self.assertTrue(is_decimal('+123'))
        self.assertFalse(is_decimal('-123.0'))
        self.assertFalse(is_decimal('+123.0'))
        self.assertFalse(is_decimal('123e4'))
        self.assertFalse(is_decimal('123E4'))
        self.assertFalse(is_decimal('123.'))
        self.assertFalse(is_decimal('123..'))
        self.assertFalse(is_decimal('123.123'))
        self.assertFalse(is_decimal('123.123456789'))

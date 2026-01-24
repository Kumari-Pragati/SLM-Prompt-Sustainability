import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_simple_decimal(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('456.78'))
        self.assertTrue(is_decimal('0'))

    def test_edge_cases(self):
        self.assertTrue(is_decimal('1234567890'))
        self.assertTrue(is_decimal('123.45'))
        self.assertFalse(is_decimal('12345678901'))
        self.assertFalse(is_decimal('123.456'))
        self.assertFalse(is_decimal('123.456789'))
        self.assertFalse(is_decimal('123.45e-1'))
        self.assertFalse(is_decimal('123.45E-1'))
        self.assertFalse(is_decimal('123.45e+1'))
        self.assertFalse(is_decimal('123.45E+1'))

    def test_complex_cases(self):
        self.assertTrue(is_decimal('+123'))
        self.assertTrue(is_decimal('-123'))
        self.assertTrue(is_decimal('123.45e+000'))
        self.assertTrue(is_decimal('123.45e-000'))
        self.assertFalse(is_decimal('123a'))
        self.assertFalse(is_decimal('123z'))
        self.assertFalse(is_decimal('123_'))
        self.assertFalse(is_decimal('123-'))
        self.assertFalse(is_decimal('123.'))
        self.assertFalse(is_decimal('123..'))
        self.assertFalse(is_decimal('123e'))
        self.assertFalse(is_decimal('123E'))
        self.assertFalse(is_decimal('123e+'))
        self.assertFalse(is_decimal('123e-'))

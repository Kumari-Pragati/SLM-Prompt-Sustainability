import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_simple_decimal(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('456.78'))
        self.assertTrue(is_decimal('0'))

    def test_edge_cases(self):
        self.assertTrue(is_decimal('1234567890'))
        self.assertTrue(is_decimal('0.1'))
        self.assertFalse(is_decimal('123.456789'))
        self.assertFalse(is_decimal('123.456'))
        self.assertFalse(is_decimal('123.4567890123'))
        self.assertFalse(is_decimal('123.0'))
        self.assertFalse(is_decimal('123e4'))
        self.assertFalse(is_decimal('123E4'))
        self.assertFalse(is_decimal('123.456Z'))
        self.assertFalse(is_decimal('123.456-'))

    def test_complex_cases(self):
        self.assertTrue(is_decimal('+123'))
        self.assertTrue(is_decimal('-123'))
        self.assertTrue(is_decimal('123.45e-2'))
        self.assertTrue(is_decimal('123.45E-2'))
        self.assertFalse(is_decimal('123.45e+2'))
        self.assertFalse(is_decimal('123.45E+2'))
        self.assertFalse(is_decimal('123.45e-invalidexponent'))
        self.assertFalse(is_decimal('123.45E-invalidexponent'))
        self.assertFalse(is_decimal('123.45z'))
        self.assertFalse(is_decimal('123.45-'))
        self.assertFalse(is_decimal('123.45a'))
        self.assertFalse(is_decimal('123.45_'))

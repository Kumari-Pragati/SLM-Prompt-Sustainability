import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('0'))
        self.assertTrue(is_decimal('123.0'))

    def test_edge_and_boundary_cases(self):
        self.assertFalse(is_decimal('-123'))
        self.assertFalse(is_decimal('123e4'))
        self.assertFalse(is_decimal('123.456'))
        self.assertFalse(is_decimal('123.000'))
        self.assertFalse(is_decimal('123.00'))
        self.assertFalse(is_decimal('123.'))
        self.assertFalse(is_decimal('123abc'))
        self.assertFalse(is_decimal('123_45'))
        self.assertFalse(is_decimal('123-45'))
        self.assertFalse(is_decimal('123+45'))
        self.assertFalse(is_decimal('123e-4'))
        self.assertFalse(is_decimal('123e+4'))
        self.assertFalse(is_decimal('123.123'))
        self.assertFalse(is_decimal('123.123e-4'))
        self.assertFalse(is_decimal('123.123e+4'))

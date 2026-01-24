import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_normal_input(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('123.0'))

    def test_edge_cases(self):
        self.assertTrue(is_decimal('1234567890123456789'))
        self.assertTrue(is_decimal('0'))
        self.assertTrue(is_decimal('0.1'))
        self.assertTrue(is_decimal('999.99'))
        self.assertFalse(is_decimal('12345678901234567890'))

    def test_boundary_cases(self):
        self.assertTrue(is_decimal('123.456'))
        self.assertTrue(is_decimal('123.00'))
        self.assertFalse(is_decimal('123.'))
        self.assertFalse(is_decimal('123.4'))
        self.assertFalse(is_decimal('123.456789'))

    def test_invalid_inputs(self):
        self.assertFalse(is_decimal('abc123'))
        self.assertFalse(is_decimal('123a'))
        self.assertFalse(is_decimal('123z'))
        self.assertFalse(is_decimal('123-'))
        self.assertFalse(is_decimal('123e'))

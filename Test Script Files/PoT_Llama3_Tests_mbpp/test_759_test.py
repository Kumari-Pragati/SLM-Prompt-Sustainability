import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('123.'))
        self.assertTrue(is_decimal('0'))

    def test_edge_cases(self):
        self.assertFalse(is_decimal('123abc'))
        self.assertFalse(is_decimal('123.abc'))
        self.assertFalse(is_decimal('.123'))
        self.assertFalse(is_decimal('123..'))

    def test_boundary_cases(self):
        self.assertTrue(is_decimal('0.00'))
        self.assertTrue(is_decimal('12345678901234567890'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_decimal(None)
        with self.assertRaises(TypeError):
            is_decimal('')

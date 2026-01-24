import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('0'))
        self.assertTrue(is_decimal('12345678901234567890'))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(is_decimal(''))
        self.assertFalse(is_decimal('.'))
        self.assertFalse(is_decimal('123abc'))
        self.assertFalse(is_decimal('123.456abc'))

    def test_invalid_inputs(self):
        self.assertFalse(is_decimal(None))
        self.assertFalse(is_decimal('abc'))
        self.assertFalse(is_decimal('123abc'))

import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_valid_decimal(self):
        self.assertTrue(is_decimal('12'))
        self.assertTrue(is_decimal('12.34'))
        self.assertTrue(is_decimal('12345678901234567890'))

    def test_invalid_input(self):
        self.assertFalse(is_decimal('abc'))
        self.assertFalse(is_decimal('123abc'))
        self.assertFalse(is_decimal('12.34abc'))

    def test_edge_cases(self):
        self.assertTrue(is_decimal('0'))
        self.assertTrue(is_decimal('0.00'))
        self.assertFalse(is_decimal(''))
        self.assertFalse(is_decimal('.'))
        self.assertFalse(is_decimal('123.456abc'))

    def test_boundary_cases(self):
        self.assertTrue(is_decimal('99999999999999999999'))
        self.assertTrue(is_decimal('12345678901234567890.12345678901234567890'))

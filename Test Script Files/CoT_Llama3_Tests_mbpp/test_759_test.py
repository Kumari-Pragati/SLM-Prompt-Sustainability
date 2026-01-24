import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_true_decimals(self):
        self.assertTrue(is_decimal('12'))
        self.assertTrue(is_decimal('12.34'))
        self.assertTrue(is_decimal('12345678901234567890'))

    def test_false_non_decimal(self):
        self.assertFalse(is_decimal('abc'))
        self.assertFalse(is_decimal('123abc'))
        self.assertFalse(is_decimal('abc123'))

    def test_false_non_numeric(self):
        self.assertFalse(is_decimal(''))
        self.assertFalse(is_decimal(None))
        self.assertFalse(is_decimal('   '))

    def test_edge_cases(self):
        self.assertTrue(is_decimal('0'))
        self.assertTrue(is_decimal('0.00'))
        self.assertFalse(is_decimal('.'))
        self.assertFalse(is_decimal('123..456'))

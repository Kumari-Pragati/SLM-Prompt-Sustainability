import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_typical_decimal(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('0.12'))

    def test_typical_non_decimal(self):
        self.assertFalse(is_decimal('abc'))
        self.assertFalse(is_decimal('123abc'))
        self.assertFalse(is_decimal('123.abc'))

    def test_edge_case_empty(self):
        self.assertFalse(is_decimal(''))
        self.assertFalse(is_decimal('.'))

    def test_edge_case_single_digit(self):
        self.assertTrue(is_decimal('1'))
        self.assertFalse(is_decimal('.'))

    def test_edge_case_multiple_dots(self):
        self.assertFalse(is_decimal('..'))
        self.assertFalse(is_decimal('123..'))

    def test_edge_case_trailing_dot(self):
        self.assertTrue(is_decimal('123.'))
        self.assertFalse(is_decimal('123..'))

    def test_edge_case_leading_dot(self):
        self.assertFalse(is_decimal('.123'))

    def test_edge_case_multiple_dots_and_digits(self):
        self.assertTrue(is_decimal('123.45'))
        self.assertFalse(is_decimal('123..45'))

import unittest
from mbpp_759_code import is_decimal

class TestIsDecimal(unittest.TestCase):

    def test_valid_decimal(self):
        self.assertTrue(is_decimal("123"))
        self.assertTrue(is_decimal("123.45"))
        self.assertTrue(is_decimal("123."))
        self.assertTrue(is_decimal("123"))

    def test_invalid_decimal(self):
        self.assertFalse(is_decimal("123abc"))
        self.assertFalse(is_decimal("123.abc"))
        self.assertFalse(is_decimal(".45"))
        self.assertFalse(is_decimal("123abc"))

    def test_edge_cases(self):
        self.assertTrue(is_decimal("0"))
        self.assertTrue(is_decimal("0."))
        self.assertFalse(is_decimal(""))

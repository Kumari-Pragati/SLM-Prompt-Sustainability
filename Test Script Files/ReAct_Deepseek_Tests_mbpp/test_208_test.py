import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('0.0'))
        self.assertTrue(is_decimal('123'))

    def test_edge_cases(self):
        self.assertFalse(is_decimal('123.456'))
        self.assertFalse(is_decimal('123.'))
        self.assertFalse(is_decimal('123.457'))
        self.assertFalse(is_decimal('123.4567'))
        self.assertFalse(is_decimal(''))
        self.assertFalse(is_decimal('123.45.67'))
        self.assertFalse(is_decimal('123.45a'))
        self.assertFalse(is_decimal('a123.45'))
        self.assertFalse(is_decimal('a123.45b'))
        self.assertFalse(is_decimal('123abc'))
        self.assertFalse(is_decimal('abc123.45'))

    def test_explicitly_handled_error_cases(self):
        self.assertFalse(is_decimal(None))
        self.assertFalse(is_decimal(123.45))
        self.assertFalse(is_decimal([1, 2, 3]))
        self.assertFalse(is_decimal({'key': 'value'}))

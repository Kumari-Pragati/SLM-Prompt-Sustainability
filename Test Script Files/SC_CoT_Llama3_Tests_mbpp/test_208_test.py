import unittest
from mbpp_208_code import is_decimal

class TestIsDecimal(unittest.TestCase):
    def test_typical_decimal(self):
        self.assertTrue(is_decimal('123'))
        self.assertTrue(is_decimal('123.45'))
        self.assertTrue(is_decimal('12.34'))

    def test_edge_cases(self):
        self.assertFalse(is_decimal(''))
        self.assertFalse(is_decimal('abc'))
        self.assertFalse(is_decimal('123abc'))
        self.assertFalse(is_decimal('.45'))
        self.assertFalse(is_decimal('123.4567'))

    def test_decimal_with_trailing_zeros(self):
        self.assertTrue(is_decimal('12300'))
        self.assertTrue(is_decimal('123.4500'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_decimal(None)
        with self.assertRaises(TypeError):
            is_decimal([])
        with self.assertRaises(TypeError):
            is_decimal({'a': 'b'})

    def test_non_string_inputs(self):
        with self.assertRaises(TypeError):
            is_decimal(123)
        with self.assertRaises(TypeError):
            is_decimal(123.45)

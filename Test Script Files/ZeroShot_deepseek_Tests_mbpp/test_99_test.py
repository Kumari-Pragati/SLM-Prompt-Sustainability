import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_decimal_to_binary_positive(self):
        self.assertEqual(decimal_to_binary(10), '1010')
        self.assertEqual(decimal_to_binary(20), '10100')
        self.assertEqual(decimal_to_binary(100), '1100100')

    def test_decimal_to_binary_zero(self):
        self.assertEqual(decimal_to_binary(0), '0')

    def test_decimal_to_binary_negative(self):
        self.assertEqual(decimal_to_binary(-10), '-1010')
        self.assertEqual(decimal_to_binary(-20), '-10100')
        self.assertEqual(decimal_to_binary(-100), '-1100100')

    def test_decimal_to_binary_non_integer(self):
        with self.assertRaises(TypeError):
            decimal_to_binary(10.5)

    def test_decimal_to_binary_large_number(self):
        self.assertEqual(decimal_to_binary(10**10), '1010000000000000000000000000000000')

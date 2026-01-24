import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(1), '1')
        self.assertEqual(decimal_to_binary(2), '10')
        self.assertEqual(decimal_to_binary(3), '11')
        self.assertEqual(decimal_to_binary(4), '100')
        self.assertEqual(decimal_to_binary(5), '101')

    def test_negative_integers(self):
        self.assertRaises(OverflowError, decimal_to_binary, -1)

    def test_non_integer(self):
        self.assertRaises(TypeError, decimal_to_binary, 'a')

    def test_large_integer(self):
        self.assertEqual(decimal_to_binary(2**31 - 1), '1111111111111111111111111111111')

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), '0')

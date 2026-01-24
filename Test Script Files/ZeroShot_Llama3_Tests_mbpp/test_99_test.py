import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(decimal_to_binary(1), '1')
        self.assertEqual(decimal_to_binary(2), '10')
        self.assertEqual(decimal_to_binary(3), '11')
        self.assertEqual(decimal_to_binary(4), '100')
        self.assertEqual(decimal_to_binary(5), '101')

    def test_negative_integer(self):
        self.assertEqual(decimal_to_binary(-1), '-1')
        self.assertEqual(decimal_to_binary(-2), '-10')
        self.assertEqual(decimal_to_binary(-3), '-11')
        self.assertEqual(decimal_to_binary(-4), '-100')
        self.assertEqual(decimal_to_binary(-5), '-101')

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), '0')

    def test_non_integer(self):
        self.assertEqual(decimal_to_binary(1.5), '1')
        self.assertEqual(decimal_to_binary(-1.5), '-1')
        self.assertEqual(decimal_to_binary(0.5), '0')
        self.assertEqual(decimal_to_binary(-0.5), '0')

    def test_large_integer(self):
        self.assertEqual(decimal_to_binary(2**31 - 1), '11111111111111111111111111111111')
        self.assertEqual(decimal_to_binary(-2**31), '-11111111111111111111111111111111')

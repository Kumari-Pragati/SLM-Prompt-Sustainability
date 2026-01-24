import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), '0')

    def test_one(self):
        self.assertEqual(decimal_to_binary(1), '1')

    def test_two(self):
        self.assertEqual(decimal_to_binary(2), '10')

    def test_three(self):
        self.assertEqual(decimal_to_binary(3), '11')

    def test_four(self):
        self.assertEqual(decimal_to_binary(4), '100')

    def test_five(self):
        self.assertEqual(decimal_to_binary(5), '101')

    def test_negative_numbers(self):
        self.assertEqual(decimal_to_binary(-1), '1')
        self.assertEqual(decimal_to_binary(-2), '10')
        self.assertEqual(decimal_to_binary(-3), '11')
        self.assertEqual(decimal_to_binary(-4), '100')
        self.assertEqual(decimal_to_binary(-5), '101')

    def test_large_numbers(self):
        self.assertEqual(decimal_to_binary(10), '1010')
        self.assertEqual(decimal_to_binary(12), '1100')
        self.assertEqual(decimal_to_binary(15), '1111')
        self.assertEqual(decimal_to_binary(255), '11111111')
        self.assertEqual(decimal_to_binary(256), '10000000')

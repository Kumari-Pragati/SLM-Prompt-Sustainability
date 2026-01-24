import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(1), '1')
        self.assertEqual(decimal_to_binary(2), '10')
        self.assertEqual(decimal_to_binary(3), '11')
        self.assertEqual(decimal_to_binary(12), '1110')
        self.assertEqual(decimal_to_binary(255), '11111111')
        self.assertEqual(decimal_to_binary(1023), '101010101')

    def test_zero_and_negative_numbers(self):
        self.assertEqual(decimal_to_binary(-1), '10' + '0' * (31)  # 32-bit negative number
        self.assertEqual(decimal_to_binary(0), '0')

    def test_large_numbers(self):
        self.assertEqual(decimal_to_binary(2**32 - 1), '1' + '0' * 31)  # Maximum positive 32-bit integer
        self.assertEqual(decimal_to_binary(2**64 - 1), '1' + '0' * 63)  # Maximum positive 64-bit integer

    def test_floats(self):
        self.assertRaises(TypeError, decimal_to_binary, 3.14)

    def test_strings(self):
        self.assertRaises(TypeError, decimal_to_binary, 'abc')

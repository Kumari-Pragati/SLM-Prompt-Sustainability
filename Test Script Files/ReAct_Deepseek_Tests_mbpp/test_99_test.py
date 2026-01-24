import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_positive_decimal(self):
        self.assertEqual(decimal_to_binary(10), '1010')
        self.assertEqual(decimal_to_binary(25), '11001')
        self.assertEqual(decimal_to_binary(127), '1111111')

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), '0')

    def test_negative_decimal(self):
        # The function does not handle negative numbers, so this is an edge case
        with self.assertRaises(ValueError):
            decimal_to_binary(-10)

    def test_non_integer_input(self):
        # The function does not handle non-integer inputs, so this is an edge case
        with self.assertRaises(TypeError):
            decimal_to_binary(10.5)

    def test_large_number(self):
        # This is an edge case to test the function's performance with large numbers
        self.assertEqual(decimal_to_binary(10**1000), '1' + '0'*1000)

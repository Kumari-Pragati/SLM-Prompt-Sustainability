import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):

    def test_binary_to_decimal_single_digit(self):
        self.assertEqual(binary_to_decimal(0), 0)
        self.assertEqual(binary_to_decimal(1), 1)

    def test_binary_to_decimal_multiple_digits(self):
        self.assertEqual(binary_to_decimal(1010), 10)
        self.assertEqual(binary_to_decimal(1111), 15)
        self.assertEqual(binary_to_decimal(1001), 9)

    def test_binary_to_decimal_with_leading_zeros(self):
        self.assertEqual(binary_to_decimal(001010), 10)
        self.assertEqual(binary_to_decimal(000000), 0)

    def test_binary_to_decimal_with_invalid_input(self):
        with self.assertRaises(TypeError):
            binary_to_decimal("1010")
        with self.assertRaises(ValueError):
            binary_to_decimal(1010101010101010101010101010101010101010101010101010101010101010)

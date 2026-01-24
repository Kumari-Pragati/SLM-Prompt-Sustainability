import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):

    def test_binary_to_decimal_valid_input(self):
        self.assertEqual(binary_to_decimal('101'), 5)
        self.assertEqual(binary_to_decimal('110'), 6)
        self.assertEqual(binary_to_decimal('111'), 7)

    def test_binary_to_decimal_zero_input(self):
        self.assertEqual(binary_to_decimal('0'), 0)

    def test_binary_to_decimal_single_bit_input(self):
        self.assertEqual(binary_to_decimal('1'), 1)
        self.assertEqual(binary_to_decimal('0'), 0)

    def test_binary_to_decimal_multiple_bits_input(self):
        self.assertEqual(binary_to_decimal('1010'), 10)
        self.assertEqual(binary_to_decimal('1111'), 15)

    def test_binary_to_decimal_invalid_input(self):
        with self.assertRaises(TypeError):
            binary_to_decimal('abc')
        with self.assertRaises(TypeError):
            binary_to_decimal(None)
        with self.assertRaises(TypeError):
            binary_to_decimal(123)

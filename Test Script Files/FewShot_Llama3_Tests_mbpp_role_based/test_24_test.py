import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):
    def test_binary_to_decimal_valid_input(self):
        self.assertEqual(binary_to_decimal("101"), 5)

    def test_binary_to_decimal_zero(self):
        self.assertEqual(binary_to_decimal("0"), 0)

    def test_binary_to_decimal_single_bit(self):
        self.assertEqual(binary_to_decimal("1"), 1)

    def test_binary_to_decimal_multiple_bits(self):
        self.assertEqual(binary_to_decimal("110"), 6)

    def test_binary_to_decimal_invalid_input(self):
        with self.assertRaises(TypeError):
            binary_to_decimal("abc")

import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):

    def test_binary_to_decimal_typical_case(self):
        self.assertEqual(binary_to_decimal(1010), 10)

    def test_binary_to_decimal_single_digit(self):
        self.assertEqual(binary_to_decimal(1), 1)
        self.assertEqual(binary_to_decimal(0), 0)

    def test_binary_to_decimal_multiple_digits(self):
        self.assertEqual(binary_to_decimal(1010101010), 345)

    def test_binary_to_decimal_edge_cases(self):
        self.assertEqual(binary_to_decimal(2001), 9)
        self.assertEqual(binary_to_decimal(10000000000), 1024)

    def test_binary_to_decimal_invalid_inputs(self):
        with self.assertRaises(TypeError):
            binary_to_decimal('1010')
        with self.assertRaises(ValueError):
            binary_to_decimal(-1010)
        with self.assertRaises(ValueError):
            binary_to_decimal(1012)

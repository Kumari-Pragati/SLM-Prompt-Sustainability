import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(binary_to_decimal(""), 0)

    def test_single_digit(self):
        test_cases = [(str(i), i) for i in range(10)]
        for binary, decimal in test_cases:
            self.assertEqual(binary_to_decimal(binary), decimal)

    def test_multiple_digits(self):
        test_cases = [("1010", 10), ("1101", 13), ("10110", 22), ("11111111", 127)]
        for binary, decimal in test_cases:
            self.assertEqual(binary_to_decimal(binary), decimal)

    def test_leading_zeros(self):
        test_cases = [("0101", 5), ("00101", 5), ("000101", 5)]
        for binary, decimal in test_cases:
            self.assertEqual(binary_to_decimal(binary), decimal)

    def test_trailing_zeros(self):
        test_cases = [("10100", 10), ("11010", 26), ("101100", 22)]
        for binary, decimal in test_cases:
            self.assertEqual(binary_to_decimal(binary), decimal)

    def test_all_zeros(self):
        self.assertEqual(binary_to_decimal("0"), 0)

    def test_all_ones(self):
        self.assertEqual(binary_to_decimal("1"), 1)
        self.assertEqual(binary_to_decimal("11111111111111111111111111111111"), 2**32 - 1)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, binary_to_decimal, "-1")

    def test_non_binary_string(self):
        self.assertRaises(ValueError, binary_to_decimal, "a1b2c3")

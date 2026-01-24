import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):
    def test_valid_binary_numbers(self):
        self.assertEqual(binary_to_decimal(10), 2)
        self.assertEqual(binary_to_decimal(100), 4)
        self.assertEqual(binary_to_decimal(1010), 10)
        self.assertEqual(binary_to_decimal(10001), 17)

    def test_empty_binary_number(self):
        self.assertEqual(binary_to_decimal(''), 0)

    def test_binary_number_with_only_zeros(self):
        self.assertEqual(binary_to_decimal('0'), 0)

    def test_binary_number_with_only_ones(self):
        self.assertEqual(binary_to_decimal('1'), 1)

    def test_binary_number_with_leading_zeros(self):
        self.assertEqual(binary_to_decimal('001'), 1)

    def test_binary_number_with_leading_ones(self):
        self.assertEqual(binary_to_decimal('100'), 4)

    def test_binary_number_with_trailing_zeros(self):
        self.assertEqual(binary_to_decimal('10'), 2)

    def test_binary_number_with_trailing_ones(self):
        self.assertEqual(binary_to_decimal('11'), 3)

    def test_binary_number_with_multiple_leading_and_trailing_zeros(self):
        self.assertEqual(binary_to_decimal('00100'), 4)

    def test_binary_number_with_multiple_leading_and_trailing_ones(self):
        self.assertEqual(binary_to_decimal('111111'), 64)

    def test_binary_number_with_long_length(self):
        self.assertEqual(binary_to_decimal('10101010101010101010101010101010'), 1024)

    def test_invalid_binary_number(self):
        self.assertRaises(ValueError, binary_to_decimal, '101010101010101010101010101010x10')

import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):

    def test_empty_binary(self):
        """Test if function returns 0 for an empty binary string."""
        self.assertEqual(binary_to_decimal(""), 0)

    def test_single_digit(self):
        """Test if function correctly converts single-digit binary numbers."""
        for test_case in [(1, 1), (2, 2), (3, 4), (4, 8), (5, 10), (6, 12), (7, 14), (8, 16)]:
            self.assertEqual(binary_to_decimal(test_case[0]), test_case[1])

    def test_multiple_digits(self):
        """Test if function correctly converts multiple-digit binary numbers."""
        for test_case in [(1010, 10), (1101, 13), (10110, 22), (11111111, 255)]:
            self.assertEqual(binary_to_decimal(test_case[0]), test_case[1])

    def test_leading_zeros(self):
        """Test if function correctly handles leading zeros in binary numbers."""
        for test_case in [(010, 2), (0010, 2), (00010, 2), (000010, 2)]:
            self.assertEqual(binary_to_decimal(test_case[0]), test_case[1])

    def test_negative_binary(self):
        """Test if function correctly handles negative binary numbers."""
        with self.assertRaises(ValueError):
            binary_to_decimal("-1")

    def test_non_binary_input(self):
        """Test if function correctly handles non-binary input."""
        with self.assertRaises(ValueError):
            binary_to_decimal("123")

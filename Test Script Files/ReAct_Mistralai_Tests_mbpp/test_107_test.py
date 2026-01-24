import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):

    def test_empty_range(self):
        self.assertEqual(count_Hexadecimal(0, 0), 0)

    def test_single_hex_number(self):
        self.assertEqual(count_Hexadecimal(10, 10), 1)

    def test_single_decimal_number(self):
        self.assertEqual(count_Hexadecimal(10, 9), 0)

    def test_single_number_greater_than_15(self):
        self.assertEqual(count_Hexadecimal(16, 16), 1)

    def test_multiple_hex_numbers(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_multiple_decimal_numbers(self):
        self.assertEqual(count_Hexadecimal(1, 9), 0)

    def test_multiple_numbers_with_hex_and_decimal(self):
        self.assertEqual(count_Hexadecimal(10, 20), 6)

    def test_large_range_with_hex_numbers(self):
        self.assertEqual(count_Hexadecimal(10, 100), 25)

    def test_large_range_with_only_hex_numbers(self):
        self.assertEqual(count_Hexadecimal(10, 1000), 250)

    def test_large_range_with_only_decimal_numbers(self):
        self.assertEqual(count_Hexadecimal(1, 1000), 0)

    def test_large_range_with_hex_and_decimal_numbers(self):
        self.assertEqual(count_Hexadecimal(10, 1000), 250)

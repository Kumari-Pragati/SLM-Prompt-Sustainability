import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(decimal_To_Binary(10), 1010)

    def test_zero(self):
        self.assertEqual(decimal_To_Binary(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(decimal_To_Binary(-10), -1010)

    def test_edge_case(self):
        self.assertEqual(decimal_To_Binary(1), 1)

    def test_large_number(self):
        self.assertEqual(decimal_To_Binary(1024), 10000000000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decimal_To_Binary("abc")

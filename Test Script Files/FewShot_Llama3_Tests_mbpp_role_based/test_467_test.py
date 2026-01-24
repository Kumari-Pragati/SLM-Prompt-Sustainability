import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):
    def test_positive_decimal(self):
        self.assertEqual(decimal_to_Octal(10), 12)

    def test_zero_decimal(self):
        self.assertEqual(decimal_to_Octal(0), 0)

    def test_negative_decimal(self):
        self.assertEqual(decimal_to_Octal(-10), -12)

    def test_large_decimal(self):
        self.assertEqual(decimal_to_Octal(1000), 1024)

    def test_edge_case_decimal(self):
        self.assertEqual(decimal_to_Octal(8), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decimal_to_Octal('a')

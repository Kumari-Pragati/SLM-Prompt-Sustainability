import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(decimal_To_Binary(10), 1010)

    def test_negative_integer(self):
        with self.assertRaises(OverflowError):
            decimal_To_Binary(-10)

    def test_zero(self):
        self.assertEqual(decimal_To_Binary(0), 0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            decimal_To_Binary('10')

    def test_large_integer(self):
        self.assertEqual(decimal_To_Binary(1024), 10000000000)

    def test_binary_string(self):
        self.assertEqual(decimal_To_Binary(2), 10)

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

    def test_single_bit(self):
        self.assertEqual(decimal_To_Binary(1), 1)

    def test_multiple_bits(self):
        self.assertEqual(decimal_To_Binary(15), 1111)

    def test_max_value(self):
        self.assertEqual(decimal_To_Binary(2**31-1), 1111111111111111011111111111111)

    def test_max_value_plus_one(self):
        with self.assertRaises(OverflowError):
            decimal_To_Binary(2**31)

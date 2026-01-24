import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(decimal_To_Binary(10), 1010)
        self.assertEqual(decimal_To_Binary(255), 11111111)
        self.assertEqual(decimal_To_Binary(1024), 10000000)

    def test_zero(self):
        self.assertEqual(decimal_To_Binary(0), '0')

    def test_negative_numbers(self):
        self.assertEqual(decimal_To_Binary(-1), '10000001')
        self.assertEqual(decimal_To_Binary(-10), '1010101010')
        self.assertEqual(decimal_To_Binary(-1024), '100000001000')

    def test_large_numbers(self):
        self.assertEqual(decimal_To_Binary(2**31 - 1), '10000000000000000000000000000001')
        self.assertEqual(decimal_To_Binary(2**64 - 1), '1' + '0' * 63)

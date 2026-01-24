import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(decimal_To_Binary(1), 1)
        self.assertEqual(decimal_To_Binary(2), 10)
        self.assertEqual(decimal_To_Binary(3), 11)
        self.assertEqual(decimal_To_Binary(4), 100)
        self.assertEqual(decimal_To_Binary(5), 101)
        self.assertEqual(decimal_To_Binary(6), 110)
        self.assertEqual(decimal_To_Binary(7), 111)
        self.assertEqual(decimal_To_Binary(8), 1000)
        self.assertEqual(decimal_To_Binary(9), 1001)
        self.assertEqual(decimal_To_Binary(10), 1010)
        self.assertEqual(decimal_To_Binary(11), 1011)
        self.assertEqual(decimal_To_Binary(12), 1100)
        self.assertEqual(decimal_To_Binary(13), 1101)
        self.assertEqual(decimal_To_Binary(14), 1110)
        self.assertEqual(decimal_To_Binary(15), 1111)
        self.assertEqual(decimal_To_Binary(16), 10000)

    def test_zero_and_one(self):
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(1), 1)

    def test_large_numbers(self):
        self.assertEqual(decimal_To_Binary(255), 11111110)
        self.assertEqual(decimal_To_Binary(256), 100000000)
        self.assertEqual(decimal_To_Binary(511), 1111111111)
        self.assertEqual(decimal_To_Binary(1023), 11111111111)
        self.assertEqual(decimal_To_Binary(1024), 10000000000)
        self.assertEqual(decimal_To_Binary(2047), 11111111111111)

    def test_negative_numbers(self):
        self.assertEqual(decimal_To_Binary(-1), 'Error: Negative numbers are not supported')
        self.assertEqual(decimal_To_Binary(-2), 'Error: Negative numbers are not supported')
        self.assertEqual(decimal_To_Binary(-3), 'Error: Negative numbers are not supported')
        self.assertEqual(decimal_To_Binary(-4), 'Error: Negative numbers are not supported')
        self.assertEqual(decimal_To_Binary(-5), 'Error: Negative numbers are not supported')
        self.assertEqual(decimal_To_Binary(-6), 'Error: Negative numbers are not supported')
        self.assertEqual(decimal_To_Binary(-7), 'Error: Negative numbers are not supported')
        self.assertEqual(decimal_To_Binary(-8), 'Error: Negative numbers are not supported')
        self.assertEqual(decimal_To_Binary(-9), 'Error: Negative numbers are not supported')
        self.assertEqual(decimal_To_Binary(-10), 'Error: Negative numbers are not supported')

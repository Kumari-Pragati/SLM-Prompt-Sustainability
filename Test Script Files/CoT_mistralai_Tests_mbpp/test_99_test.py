import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(decimal_to_binary(0), "0")
        self.assertEqual(decimal_to_binary(1), "1")
        self.assertEqual(decimal_to_binary(2), "10")
        self.assertEqual(decimal_to_binary(3), "11")
        self.assertEqual(decimal_to_binary(4), "100")
        self.assertEqual(decimal_to_binary(5), "101")
        self.assertEqual(decimal_to_binary(6), "110")
        self.assertEqual(decimal_to_binary(7), "111")
        self.assertEqual(decimal_to_binary(8), "1000")
        self.assertEqual(decimal_to_binary(9), "1001")
        self.assertEqual(decimal_to_binary(10), "1010")
        self.assertEqual(decimal_to_binary(11), "1011")
        self.assertEqual(decimal_to_binary(12), "1100")
        self.assertEqual(decimal_to_binary(13), "1101")
        self.assertEqual(decimal_to_binary(14), "1110")
        self.assertEqual(decimal_to_binary(15), "1111")
        self.assertEqual(decimal_to_binary(16), "10000")
        self.assertEqual(decimal_to_binary(255), "11111111")
        self.assertEqual(decimal_to_binary(256), "10000000")

    def test_negative_numbers(self):
        self.assertEqual(decimal_to_binary(-1), "10000001")
        self.assertEqual(decimal_to_binary(-2), "10000010")
        self.assertEqual(decimal_to_binary(-3), "10000011")
        self.assertEqual(decimal_to_binary(-4), "10000100")
        self.assertEqual(decimal_to_binary(-5), "10000101")
        self.assertEqual(decimal_to_binary(-6), "10000110")
        self.assertEqual(decimal_to_binary(-7), "10000111")
        self.assertEqual(decimal_to_binary(-8), "10001000")
        self.assertEqual(decimal_to_binary(-9), "10001001")
        self.assertEqual(decimal_to_binary(-10), "10001010")
        self.assertEqual(decimal_to_binary(-11), "10001011")
        self.assertEqual(decimal_to_binary(-12), "10001100")
        self.assertEqual(decimal_to_binary(-13), "10001101")
        self.assertEqual(decimal_to_binary(-14), "10001110")
        self.assertEqual(decimal_to_binary(-15), "10001111")
        self.assertEqual(decimal_to_binary(-16), "10010000")
        self.assertEqual(decimal_to_binary(-255), "11111111111111111111111111111111")
        self.assertEqual(decimal_to_binary(-256), "10000000000000000000000000000001")

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "0")

    def test_large_numbers(self):
        self.assertEqual(decimal_
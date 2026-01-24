import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(decimal_To_Binary(0), 0)

    def test_one(self):
        self.assertEqual(decimal_To_Binary(1), 1)

    def test_two(self):
        self.assertEqual(decimal_To_Binary(2), 10)

    def test_three(self):
        self.assertEqual(decimal_To_Binary(3), 11)

    def test_four(self):
        self.assertEqual(decimal_To_Binary(4), 100)

    def test_five(self):
        self.assertEqual(decimal_To_Binary(5), 101)

    def test_eight(self):
        self.assertEqual(decimal_To_Binary(8), 1000)

    def test_negative_number(self):
        self.assertEqual(decimal_To_Binary(-1), 11111111)

    def test_large_number(self):
        self.assertEqual(decimal_To_Binary(2147483647), 111111111111111111111111)

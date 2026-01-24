import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_To_Binary(10), 1010)
        self.assertEqual(decimal_To_Binary(18), 10010)
        self.assertEqual(decimal_To_Binary(1), 1)
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(1023), 1111111111)

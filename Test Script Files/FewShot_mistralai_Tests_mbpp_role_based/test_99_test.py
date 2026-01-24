import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), '0')

    def test_one(self):
        self.assertEqual(decimal_to_binary(1), '1')

    def test_two(self):
        self.assertEqual(decimal_to_binary(2), '10')

    def test_eight(self):
        self.assertEqual(decimal_to_binary(8), '1000')

    def test_negative_number(self):
        self.assertRaises(ValueError, decimal_to_binary, -1)

    def test_large_number(self):
        self.assertRaises(ValueError, decimal_to_binary, 2**31)

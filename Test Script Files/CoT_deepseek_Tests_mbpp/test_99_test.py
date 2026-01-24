import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(decimal_to_binary(10), '1010')

    def test_boundary_conditions(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(1), '1')

    def test_large_number(self):
        self.assertEqual(decimal_to_binary(1024), '10000000000')

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            decimal_to_binary(-10)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            decimal_to_binary(10.5)

    def test_large_non_integer_input(self):
        with self.assertRaises(OverflowError):
            decimal_to_binary(10**1000)

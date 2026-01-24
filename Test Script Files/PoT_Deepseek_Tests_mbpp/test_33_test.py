import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(1), 1)
        self.assertEqual(decimal_To_Binary(2), 10)
        self.assertEqual(decimal_To_Binary(10), 1010)
        self.assertEqual(decimal_To_Binary(15), 1111)

    def test_edge_cases(self):
        self.assertEqual(decimal_To_Binary(256), 100000000)
        self.assertEqual(decimal_To_Binary(511), 111111111)

    def test_boundary_cases(self):
        self.assertEqual(decimal_To_Binary(1023), 1111111111)
        self.assertEqual(decimal_To_Binary(2047), 11111111111)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decimal_To_Binary('abc')
        with self.assertRaises(ValueError):
            decimal_To_Binary(-1)

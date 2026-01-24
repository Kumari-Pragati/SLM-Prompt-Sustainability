import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(decimal_To_Binary(10), 1010)
        self.assertEqual(decimal_To_Binary(5), 101)
        self.assertEqual(decimal_To_Binary(2), 10)

    def test_edge_cases(self):
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(1), 1)

    def test_boundary_cases(self):
        self.assertEqual(decimal_To_Binary(2**31 - 1), 1111111111111111111111111111111)
        self.assertEqual(decimal_To_Binary(2**31), 1111111111111111111111111111110)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            decimal_To_Binary('a')
        with self.assertRaises(TypeError):
            decimal_To_Binary(None)

    def test_special_cases(self):
        self.assertEqual(decimal_To_Binary(-1), -1)
        self.assertEqual(decimal_To_Binary(-2), -10)

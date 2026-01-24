import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(1), '1')
        self.assertEqual(decimal_to_binary(10), '1010')
        self.assertEqual(decimal_to_binary(255), '11111111')

    def test_edge_cases(self):
        self.assertEqual(decimal_to_binary(256), '100000000')
        self.assertEqual(decimal_to_binary(511), '111111111')

    def test_boundary_conditions(self):
        self.assertEqual(decimal_to_binary(257), '100000001')
        self.assertEqual(decimal_to_binary(1023), '1111111111')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decimal_to_binary('10')
        with self.assertRaises(TypeError):
            decimal_to_binary(None)
        with self.assertRaises(TypeError):
            decimal_to_binary([10])

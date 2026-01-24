import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(1), '1')
        self.assertEqual(decimal_to_binary(10), '1010')
        self.assertEqual(decimal_to_binary(255), '11111111')

    def test_boundary_conditions(self):
        self.assertEqual(decimal_to_binary(2**32 - 1), '1111111111111111111111111111111')
        self.assertEqual(decimal_to_binary(2**64 - 1), '111111111111111111111111111111111111111111111111111111111111111')

    def test_edge_cases(self):
        self.assertEqual(decimal_to_binary(2**64), '')
        self.assertEqual(decimal_to_binary(-1), '')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            decimal_to_binary('10')
        with self.assertRaises(TypeError):
            decimal_to_binary(None)

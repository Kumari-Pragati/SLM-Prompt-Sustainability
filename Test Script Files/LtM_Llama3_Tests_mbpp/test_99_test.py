import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(1), '1')
        self.assertEqual(decimal_to_binary(2), '10')
        self.assertEqual(decimal_to_binary(3), '11')
        self.assertEqual(decimal_to_binary(4), '100')
        self.assertEqual(decimal_to_binary(5), '101')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(255), '11111111')
        self.assertEqual(decimal_to_binary(-1), '11111111')
        self.assertEqual(decimal_to_binary(-2), '11111110')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            decimal_to_binary('a')
        with self.assertRaises(TypeError):
            decimal_to_binary(None)

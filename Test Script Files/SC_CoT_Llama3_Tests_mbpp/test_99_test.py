import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(1), '1')
        self.assertEqual(decimal_to_binary(2), '10')
        self.assertEqual(decimal_to_binary(3), '11')
        self.assertEqual(decimal_to_binary(4), '100')
        self.assertEqual(decimal_to_binary(5), '101')
        self.assertEqual(decimal_to_binary(6), '110')
        self.assertEqual(decimal_to_binary(7), '111')

    def test_edge_cases(self):
        self.assertEqual(decimal_to_binary(8), '1000')
        self.assertEqual(decimal_to_binary(15), '1111')
        self.assertEqual(decimal_to_binary(16), '10000')
        self.assertEqual(decimal_to_binary(31), '11111')
        self.assertEqual(decimal_to_binary(32), '100000')
        self.assertEqual(decimal_to_binary(255), '11111111')
        self.assertEqual(decimal_to_binary(256), '10000000')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            decimal_to_binary('a')
        with self.assertRaises(TypeError):
            decimal_to_binary(None)
        with self.assertRaises(TypeError):
            decimal_to_binary([1, 2, 3])

    def test_boundary_cases(self):
        self.assertEqual(decimal_to_binary(-1), '11111111')
        self.assertEqual(decimal_to_binary(-2), '11111110')
        self.assertEqual(decimal_to_binary(-8), '11100000')
        self.assertEqual(decimal_to_binary(-16), '10000000')
        self.assertEqual(decimal_to_binary(-32), '10000000')
        self.assertEqual(decimal_to_binary(-256), '10000000')

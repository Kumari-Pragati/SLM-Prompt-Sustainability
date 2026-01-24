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
        self.assertEqual(decimal_to_binary(6), '110')
        self.assertEqual(decimal_to_binary(7), '111')
        self.assertEqual(decimal_to_binary(8), '1000')
        self.assertEqual(decimal_to_binary(9), '1001')
        self.assertEqual(decimal_to_binary(10), '1010')
        self.assertEqual(decimal_to_binary(11), '1011')
        self.assertEqual(decimal_to_binary(12), '1100')
        self.assertEqual(decimal_to_binary(13), '1101')
        self.assertEqual(decimal_to_binary(14), '1110')
        self.assertEqual(decimal_to_binary(15), '1111')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(decimal_to_binary(-1), '1000000000000000000000001')
        self.assertEqual(decimal_to_binary(0b1000000000000000000000000), '1')
        self.assertEqual(decimal_to_binary(2**64 - 1), '1' + '0' * 63)
        self.assertEqual(decimal_to_binary(2**64), '0')

import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(1), '1')
        self.assertEqual(decimal_to_binary(2), '10')
        self.assertEqual(decimal_to_binary(3), '11')
        self.assertEqual(decimal_to_binary(10), '1010')

    def test_edge_conditions(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(1), '1')
        self.assertEqual(decimal_to_binary(255), '11111111')

    def test_boundary_conditions(self):
        self.assertEqual(decimal_to_binary(256), '100000000')
        self.assertEqual(decimal_to_binary(511), '111111111')
        self.assertEqual(decimal_to_binary(1023), '1111111111')

    def test_more_complex_cases(self):
        self.assertEqual(decimal_to_binary(1024), '10000000000')
        self.assertEqual(decimal_to_binary(2048), '100000000000')
        self.assertEqual(decimal_to_binary(4096), '1000000000000')

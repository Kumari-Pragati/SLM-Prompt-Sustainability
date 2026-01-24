import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(decimal_to_binary(10), '1010')

    def test_boundary_conditions(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(1), '1')

    def test_edge_cases(self):
        self.assertEqual(decimal_to_binary(255), '11111111')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decimal_to_binary('10')

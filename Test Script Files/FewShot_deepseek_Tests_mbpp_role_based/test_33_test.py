import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(decimal_To_Binary(10), 1010)

    def test_boundary_conditions(self):
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(1), 1)

    def test_edge_conditions(self):
        self.assertEqual(decimal_To_Binary(255), 11111111)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            decimal_To_Binary('10')
        with self.assertRaises(ValueError):
            decimal_To_Binary(-10)

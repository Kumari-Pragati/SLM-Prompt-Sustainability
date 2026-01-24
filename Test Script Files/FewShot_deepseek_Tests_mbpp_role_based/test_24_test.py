import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(binary_to_decimal(1010), 10)

    def test_edge_condition(self):
        self.assertEqual(binary_to_decimal(1), 1)

    def test_boundary_condition(self):
        self.assertEqual(binary_to_decimal(10000000000000000000000000000000), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            binary_to_decimal('1010')

        with self.assertRaises(ValueError):
            binary_to_decimal(1010101010101010101010101010101010101010101010101010101010101010)

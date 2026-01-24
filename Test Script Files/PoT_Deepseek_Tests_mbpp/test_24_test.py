import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(binary_to_decimal(1010), 10)
        self.assertEqual(binary_to_decimal(1111), 15)
        self.assertEqual(binary_to_decimal(1001), 9)

    def test_edge_cases(self):
        self.assertEqual(binary_to_decimal(0), 0)
        self.assertEqual(binary_to_decimal(1), 1)

    def test_boundary_cases(self):
        self.assertEqual(binary_to_decimal(10000), 16)
        self.assertEqual(binary_to_decimal(11111), 31)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            binary_to_decimal("1010")
        with self.assertRaises(ValueError):
            binary_to_decimal(1010101010101010101010101010101010101010101010101010101010101010)

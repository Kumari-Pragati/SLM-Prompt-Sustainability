import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(binary_to_decimal(1010), 10)

    def test_boundary_case(self):
        self.assertEqual(binary_to_decimal(0), 0)
        self.assertEqual(binary_to_decimal(1), 1)

    def test_edge_case(self):
        self.assertEqual(binary_to_decimal(11111111111111111111111111111111), 4294967295)
        self.assertEqual(binary_to_decimal(10000000000000000000000000000000), 1099511627776)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            binary_to_decimal('1010')
        with self.assertRaises(ValueError):
            binary_to_decimal(2010)
        with self.assertRaises(ValueError):
            binary_to_decimal(100000000000000000000000000000000)

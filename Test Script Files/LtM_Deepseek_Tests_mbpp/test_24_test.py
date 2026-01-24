import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):

    def test_simple_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal(1010), 10)
        self.assertEqual(binary_to_decimal(1100), 12)
        self.assertEqual(binary_to_decimal(1001), 9)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(binary_to_decimal(0), 0)
        self.assertEqual(binary_to_decimal(1), 1)
        self.assertEqual(binary_to_decimal(11111111111111111111111111111111), 4294967295)

    def test_more_complex_or_corner_cases(self):
        self.assertEqual(binary_to_decimal(10101010101010101010101010101010), 4294967290)
        self.assertEqual(binary_to_decimal(11111111111111111111111111111110), 4294967294)

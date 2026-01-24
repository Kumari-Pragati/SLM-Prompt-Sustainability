import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(binary_to_decimal("10"), 2)
        self.assertEqual(binary_to_decimal("100"), 4)
        self.assertEqual(binary_to_decimal("1010"), 10)
        self.assertEqual(binary_to_decimal("1101"), 13)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(binary_to_decimal("0"), 0)
        self.assertEqual(binary_to_decimal("1"), 1)
        self.assertEqual(binary_to_decimal("111111111111"), 255)
        self.assertEqual(binary_to_decimal("100000000000"), 1073741824)

    def test_complex_inputs(self):
        self.assertEqual(binary_to_decimal("101010101010101010101010"), 1073741820)
        self.assertEqual(binary_to_decimal("11111111111111111111111111111111"), 4294967295)
        self.assertEqual(binary_to_decimal("101010101010101010101010101010101"), 1073741821)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, binary_to_decimal, "a1b2c3")
        self.assertRaises(ValueError, binary_to_decimal, "12345")
        self.assertRaises(ValueError, binary_to_decimal, "")

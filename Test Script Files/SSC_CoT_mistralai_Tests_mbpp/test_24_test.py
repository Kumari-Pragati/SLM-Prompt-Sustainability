import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(binary_to_decimal("1010"), 10)
        self.assertEqual(binary_to_decimal("1111"), 15)
        self.assertEqual(binary_to_decimal("10001"), 17)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(binary_to_decimal("0"), 0)
        self.assertEqual(binary_to_decimal("1"), 1)
        self.assertEqual(binary_to_decimal("10000000000"), 128)
        self.assertEqual(binary_to_decimal("11111111111111111111"), 2047)

    def test_special_cases(self):
        self.assertEqual(binary_to_decimal("1000..."), 12)  # trailing zeros
        self.assertEqual(binary_to_decimal("11..."), 7)  # leading zeros

    def test_invalid_input(self):
        self.assertRaises(ValueError, binary_to_decimal, "1a")  # non-numeric characters
        self.assertRaises(ValueError, binary_to_decimal, "111111111111111111111")  # too long

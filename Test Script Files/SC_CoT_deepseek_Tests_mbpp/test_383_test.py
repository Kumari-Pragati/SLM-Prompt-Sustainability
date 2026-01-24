import unittest
from mbpp_383_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(even_bit_toggle_number(10), 14)

    def test_edge_case(self):
        self.assertEqual(even_bit_toggle_number(0), 0)

    def test_boundary_case(self):
        self.assertEqual(even_bit_toggle_number(2**31 - 1), 2**31 - 1)

    def test_corner_case(self):
        self.assertEqual(even_bit_toggle_number(2**31), 2**31)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_bit_toggle_number("invalid")

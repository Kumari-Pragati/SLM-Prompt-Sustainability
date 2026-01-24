import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(even_bit_toggle_number(10), 14)

    def test_edge_condition(self):
        self.assertEqual(even_bit_toggle_number(0), 0)

    def test_boundary_condition(self):
        self.assertEqual(even_bit_toggle_number(2**31 - 1), 2**31 - 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_bit_toggle_number("10")

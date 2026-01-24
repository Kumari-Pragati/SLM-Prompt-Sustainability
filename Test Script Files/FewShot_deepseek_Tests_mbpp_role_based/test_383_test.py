import unittest
from mbpp_383_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(even_bit_toggle_number(10), 14)

    def test_boundary_conditions(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 1)

    def test_edge_conditions(self):
        self.assertEqual(even_bit_toggle_number(255), 255)
        self.assertEqual(even_bit_toggle_number(256), 256)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            even_bit_toggle_number("10")
        with self.assertRaises(TypeError):
            even_bit_toggle_number(10.5)

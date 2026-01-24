import unittest
from mbpp_383_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 2)
        self.assertEqual(even_bit_toggle_number(2), 1)
        self.assertEqual(even_bit_toggle_number(3), 3)
        self.assertEqual(even_bit_toggle_number(10), 5)

    def test_edge_cases(self):
        self.assertEqual(even_bit_toggle_number(1 << 31), 1 << 31)
        self.assertEqual(even_bit_toggle_number(-1), -1)

    def test_boundary_cases(self):
        self.assertEqual(even_bit_toggle_number((1 << 31) - 1), (1 << 31) - 1)
        self.assertEqual(even_bit_toggle_number(1 << 31), 1 << 31)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            even_bit_toggle_number("invalid")
        with self.assertRaises(TypeError):
            even_bit_toggle_number(None)
        with self.assertRaises(TypeError):
            even_bit_toggle_number([1, 2, 3])

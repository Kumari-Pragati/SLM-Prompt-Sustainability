import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(even_bit_toggle_number(10), 14)
        self.assertEqual(even_bit_toggle_number(17), 23)
        self.assertEqual(even_bit_toggle_number(8), 12)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 1)
        self.assertEqual(even_bit_toggle_number(3), 3)
        self.assertEqual(even_bit_toggle_number(2), 2)

    def test_corner_cases(self):
        self.assertEqual(even_bit_toggle_number(15), 15)
        self.assertEqual(even_bit_toggle_number(16), 32)
        self.assertEqual(even_bit_toggle_number(31), 31)
        self.assertEqual(even_bit_toggle_number(32), 64)

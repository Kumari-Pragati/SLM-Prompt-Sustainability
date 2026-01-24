import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 2)
        self.assertEqual(even_bit_toggle_number(2), 1)
        self.assertEqual(even_bit_toggle_number(3), 3)

    def test_edge_conditions(self):
        self.assertEqual(even_bit_toggle_number(1 << 31), 1 << 31)
        self.assertEqual(even_bit_toggle_number((1 << 31) - 1), (1 << 31) - 1)

    def test_boundary_conditions(self):
        self.assertEqual(even_bit_toggle_number((1 << 31) - 1), (1 << 31) - 1)
        self.assertEqual(even_bit_toggle_number((1 << 31)), (1 << 31))

    def test_more_complex_cases(self):
        self.assertEqual(even_bit_toggle_number(15), 14)
        self.assertEqual(even_bit_toggle_number(16), 15)
        self.assertEqual(even_bit_toggle_number(17), 17)
        self.assertEqual(even_bit_toggle_number(18), 19)

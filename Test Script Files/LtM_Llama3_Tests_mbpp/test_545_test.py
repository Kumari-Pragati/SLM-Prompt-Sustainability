import unittest
from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFAndLBits(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(toggle_F_and_L_bits(0), 0)
        self.assertEqual(toggle_F_and_L_bits(1), 0)
        self.assertEqual(toggle_F_and_L_bits(2), 3)
        self.assertEqual(toggle_F_and_L_bits(3), 2)
        self.assertEqual(toggle_F_and_L_bits(4), 5)
        self.assertEqual(toggle_F_and_L_bits(5), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(toggle_F_and_L_bits(0x7fffffff), 0x7fffffff)
        self.assertEqual(toggle_F_and_L_bits(0x80000000), 0)
        self.assertEqual(toggle_F_and_L_bits(0x7fffffff + 1), 0x7fffffff)
        self.assertEqual(toggle_F_and_L_bits(0x80000000 + 1), 1)

    def test_complex_and_corner_cases(self):
        self.assertEqual(toggle_F_and_L_bits(0x7fffffff + 2), 0x7fffffff + 3)
        self.assertEqual(toggle_F_and_L_bits(0x80000000 + 2), 3)
        self.assertEqual(toggle_F_and_L_bits(0x7fffffff + 3), 0x7fffffff + 2)
        self.assertEqual(toggle_F_and_L_bits(0x80000000 + 3), 2)

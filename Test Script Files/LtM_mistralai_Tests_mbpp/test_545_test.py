import unittest
from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFAndLBits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(toggle_F_and_L_bits(0), 1)
        self.assertEqual(toggle_F_and_L_bits(1), 0)
        self.assertEqual(toggle_F_and_L_bits(3), 2)
        self.assertEqual(toggle_F_and_L_bits(5), 6)
        self.assertEqual(toggle_F_and_L_bits(7), 8)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(toggle_F_and_L_bits(2**n - 1), 2**n for n in range(1, 17))
        self.assertEqual(toggle_F_and_L_bits(2**16), 0)
        self.assertEqual(toggle_F_and_L_bits(2**32 - 1), 2**32)

    def test_complex_inputs(self):
        self.assertEqual(toggle_F_and_L_bits(0b1010_1010), 0b0101_0101)
        self.assertEqual(toggle_F_and_L_bits(0b1111_1111_1111_1101), 0b1111_1111_1111_0010)

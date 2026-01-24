import unittest
from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFAndLBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(toggle_F_and_L_bits(0), 0)
        self.assertEqual(toggle_F_and_L_bits(1), 0)
        self.assertEqual(toggle_F_and_L_bits(2), 1)
        self.assertEqual(toggle_F_and_L_bits(3), 1)
        self.assertEqual(toggle_F_and_L_bits(4), 0)
        self.assertEqual(toggle_F_and_L_bits(5), 0)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(toggle_F_and_L_bits(0xFFFFFFFF), 0)
        self.assertEqual(toggle_F_and_L_bits(0), 0)
        self.assertEqual(toggle_F_and_L_bits(1), 0)
        self.assertEqual(toggle_F_and_L_bits(0x7FFFFFFF), 0)
        self.assertEqual(toggle_F_and_L_bits(0x80000000), 1)

    def test_corner_cases(self):
        self.assertEqual(toggle_F_and_L_bits(0x00000001), 0)
        self.assertEqual(toggle_F_and_L_bits(0x00000002), 1)
        self.assertEqual(toggle_F_and_L_bits(0x00000003), 1)
        self.assertEqual(toggle_F_and_L_bits(0x00000004), 0)
        self.assertEqual(toggle_F_and_L_bits(0x00000005), 0)

import unittest
from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFAndLBits(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(toggle_F_and_L_bits(10), 6)

    def test_edge_case(self):
        self.assertEqual(toggle_F_and_L_bits(1), 0)

    def test_boundary_case(self):
        self.assertEqual(toggle_F_and_L_bits(0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            toggle_F_and_L_bits("invalid")

import unittest
from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFAndLBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(toggle_F_and_L_bits(0), 0)
        self.assertEqual(toggle_F_and_L_bits(2), 1)
        self.assertEqual(toggle_F_and_L_bits(7), 4)
        self.assertEqual(toggle_F_and_L_bits(8), 7)
        self.assertEqual(toggle_F_and_L_bits(10), 5)

    def test_edge_cases(self):
        self.assertEqual(toggle_F_and_L_bits(1), 0)
        self.assertEqual(toggle_F_and_L_bits(255), 254)
        self.assertEqual(toggle_F_and_L_bits(65535), 65534)

    def test_boundary_conditions(self):
        self.assertEqual(toggle_F_and_L_bits(65536), 65535)
        self.assertEqual(toggle_F_and_L_bits(4294967295), 4294967294)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            toggle_F_and_L_bits("invalid")
        with self.assertRaises(TypeError):
            toggle_F_and_L_bits(None)

import unittest
from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFAndLBits(unittest.TestCase):

    def test_toggle_F_and_L_bits_typical_case(self):
        self.assertEqual(toggle_F_and_L_bits(10), 6)

    def test_toggle_F_and_L_bits_edge_case_1(self):
        self.assertEqual(toggle_F_and_L_bits(0), 0)

    def test_toggle_F_and_L_bits_edge_case_2(self):
        self.assertEqual(toggle_F_and_L_bits(1), 0)

    def test_toggle_F_and_L_bits_error_case(self):
        with self.assertRaises(TypeError):
            toggle_F_and_L_bits('10')

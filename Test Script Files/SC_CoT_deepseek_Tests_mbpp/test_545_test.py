import unittest

from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFAndLBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(toggle_F_and_L_bits(0), 0)
        self.assertEqual(toggle_F_and_L_bits(2), 1)
        self.assertEqual(toggle_F_and_L_bits(8), 7)
        self.assertEqual(toggle_F_and_L_bits(10), 5)

    def test_edge_cases(self):
        self.assertEqual(toggle_F_and_L_bits(1), 0)
        self.assertEqual(toggle_F_and_L_bits(3), 1)
        self.assertEqual(toggle_F_and_L_bits(15), 14)
        self.assertEqual(toggle_F_and_L_bits(31), 30)

    def test_special_cases(self):
        self.assertEqual(toggle_F_and_L_bits(255), 254)
        self.assertEqual(toggle_F_and_L_bits(256), 255)
        self.assertEqual(toggle_F_and_L_bits(511), 510)
        self.assertEqual(toggle_F_and_L_bits(512), 511)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            toggle_F_and_L_bits('a')
        with self.assertRaises(TypeError):
            toggle_F_and_L_bits(None)

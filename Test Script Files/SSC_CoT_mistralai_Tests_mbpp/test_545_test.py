import unittest
from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFAndLBits(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(toggle_F_and_L_bits(0), 1)
        self.assertEqual(toggle_F_and_L_bits(1), 0)
        self.assertEqual(toggle_F_and_L_bits(3), 2)
        self.assertEqual(toggle_F_and_L_bits(5), 6)
        self.assertEqual(toggle_F_and_L_bits(7), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(toggle_F_and_L_bits(2**15), 2**15 ^ (2**15 | 2**14 | 2**7 | 2**4 | 2**2 | 2**1), 2**15)
        self.assertEqual(toggle_F_and_L_bits(2**16 - 1), 0)
        self.assertEqual(toggle_F_and_L_bits(2**31), 2**31 ^ (2**31 | 2**30 | 2**15 | 2**7 | 2**4 | 2**2 | 2**1), 2**31)

    def test_special_cases(self):
        self.assertEqual(toggle_F_and_L_bits(2), 3)
        self.assertEqual(toggle_F_and_L_bits(4), 6)
        self.assertEqual(toggle_F_and_L_bits(6), 7)
        self.assertEqual(toggle_F_and_L_bits(8), 9)

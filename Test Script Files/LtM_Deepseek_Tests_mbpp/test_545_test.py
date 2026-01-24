import unittest
from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFAndLBits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(toggle_F_and_L_bits(0), 0)
        self.assertEqual(toggle_F_and_L_bits(1), 0)
        self.assertEqual(toggle_F_and_L_bits(2), 1)
        self.assertEqual(toggle_F_and_L_bits(3), 2)
        self.assertEqual(toggle_F_and_L_bits(4), 3)
        self.assertEqual(toggle_F_and_L_bits(5), 4)
        self.assertEqual(toggle_F_and_L_bits(6), 5)
        self.assertEqual(toggle_F_and_L_bits(7), 6)
        self.assertEqual(toggle_F_and_L_bits(8), 7)
        self.assertEqual(toggle_F_and_L_bits(9), 8)
        self.assertEqual(toggle_F_and_L_bits(10), 9)
        self.assertEqual(toggle_F_and_L_bits(11), 10)
        self.assertEqual(toggle_F_and_L_bits(12), 11)
        self.assertEqual(toggle_F_and_L_bits(13), 12)
        self.assertEqual(toggle_F_and_L_bits(14), 13)
        self.assertEqual(toggle_F_and_L_bits(15), 14)
        self.assertEqual(toggle_F_and_L_bits(16), 15)

    def test_edge_conditions(self):
        self.assertEqual(toggle_F_and_L_bits(2**31 - 1), 2**31 - 2)
        self.assertEqual(toggle_F_and_L_bits(2**31), 2**31 - 1)
        self.assertEqual(toggle_F_and_L_bits(2**32 - 1), 2**32 - 2)
        self.assertEqual(toggle_F_and_L_bits(2**32), 2**32 - 1)

    def test_more_complex_cases(self):
        self.assertEqual(toggle_F_and_L_bits(2**63 - 1), 2**63 - 2)
        self.assertEqual(toggle_F_and_L_bits(2**63), 2**63 - 1)
        self.assertEqual(toggle_F_and_L_bits(2**64 - 1), 2**64 - 2)
        self.assertEqual(toggle_F_and_L_bits(2**64), 2**64 - 1)

import unittest
from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFAndLBits(unittest.TestCase):
    def test_toggle_0(self):
        self.assertEqual(toggle_F_and_L_bits(0), 0)

    def test_toggle_1(self):
        self.assertEqual(toggle_F_and_L_bits(1), 0)

    def test_toggle_2(self):
        self.assertEqual(toggle_F_and_L_bits(2), 3)

    def test_toggle_3(self):
        self.assertEqual(toggle_F_and_L_bits(3), 2)

    def test_toggle_4(self):
        self.assertEqual(toggle_F_and_L_bits(4), 5)

    def test_toggle_5(self):
        self.assertEqual(toggle_F_and_L_bits(5), 4)

    def test_toggle_16(self):
        self.assertEqual(toggle_F_and_L_bits(16), 17)

    def test_toggle_17(self):
        self.assertEqual(toggle_F_and_L_bits(17), 16)

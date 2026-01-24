import unittest
from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFAndLBits(unittest.TestCase):

    def test_toggle_F_and_L_bits_0(self):
        self.assertEqual(toggle_F_and_L_bits(0), 0)

    def test_toggle_F_and_L_bits_1(self):
        self.assertEqual(toggle_F_and_L_bits(1), 0)

    def test_toggle_F_and_L_bits_2(self):
        self.assertEqual(toggle_F_and_L_bits(2), 2)

    def test_toggle_F_and_L_bits_max(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 1), 2**16 - 1)

    def test_toggle_F_and_L_bits_max_plus_1(self):
        self.assertEqual(toggle_F_and_L_bits(2**16), 0)

    def test_toggle_F_and_L_bits_max_minus_1(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 2), 2**16 - 2)

    def test_toggle_F_and_L_bits_max_minus_2(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 3), 2**16 - 3)

    def test_toggle_F_and_L_bits_max_minus_3(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 4), 2**16 - 4)

    def test_toggle_F_and_L_bits_max_minus_4(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 5), 2**16 - 5)

    def test_toggle_F_and_L_bits_max_minus_5(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 6), 2**16 - 6)

    def test_toggle_F_and_L_bits_max_minus_6(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 7), 2**16 - 7)

    def test_toggle_F_and_L_bits_max_minus_7(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 8), 2**16 - 8)

    def test_toggle_F_and_L_bits_max_minus_8(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 9), 2**16 - 9)

    def test_toggle_F_and_L_bits_max_minus_9(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 10), 2**16 - 10)

    def test_toggle_F_and_L_bits_max_minus_10(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 11), 2**16 - 11)

    def test_toggle_F_and_L_bits_max_minus_11(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 12), 2**16 - 12)

    def test_toggle_F_and_L_bits_max_minus_12(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 13), 2**16 - 13)

    def test_toggle_F_and_L_bits_max_minus_13(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 14), 2**16 - 14)

    def test_toggle_F_and_L_bits_max_minus_14(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 15), 2**16 - 15)

    def test_toggle_F_and_L_bits_max_minus_15(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 16), 2**16 - 16)

    def test_toggle_F_and_L_bits_max_minus_16(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 17), 2**16 - 17)

    def test_toggle_F_and_L_bits_max_minus_17(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 18), 2**16 - 18)

    def test_toggle_F_and_L_bits_max_minus_18(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 19), 2**16 - 19)

    def test_toggle_F_and_L_bits_max_minus_19(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 20), 2**16 - 20)

    def test_toggle_F_and_L_bits_max_minus_20(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 21), 2**16 - 21)

    def test_toggle_F_and_L_bits_max_minus_21(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 22), 2**16 - 22)

    def test_toggle_F_and_L_bits_max_minus_22(self):
        self.assertEqual(toggle_F_and_L_bits(2**16 - 23),
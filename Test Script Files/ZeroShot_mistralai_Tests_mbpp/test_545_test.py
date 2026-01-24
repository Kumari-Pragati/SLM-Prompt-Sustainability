import unittest
from mbpp_545_code import toggle_F_and_L_bits, take_L_and_F_set_bits

class TestToggleFandLBits(unittest.TestCase):

    def test_take_L_and_F_set_bits(self):
        self.assertEqual(take_L_and_F_set_bits(0), 1)
        self.assertEqual(take_L_and_F_set_bits(1), 3)
        self.assertEqual(take_L_and_F_set_bits(2), 7)
        self.assertEqual(take_L_and_F_set_bits(3), 15)
        self.assertEqual(take_L_and_F_set_bits(4), 31)
        self.assertEqual(take_L_and_F_set_bits(5), 63)
        self.assertEqual(take_L_and_F_set_bits(6), 127)
        self.assertEqual(take_L_and_F_set_bits(7), 255)
        self.assertEqual(take_L_and_F_set_bits(8), 511)
        self.assertEqual(take_L_and_F_set_bits(9), 1023)
        self.assertEqual(take_L_and_F_set_bits(10), 2047)
        self.assertEqual(take_L_and_F_set_bits(11), 4095)
        self.assertEqual(take_L_and_F_set_bits(12), 8191)
        self.assertEqual(take_L_and_F_set_bits(13), 16383)
        self.assertEqual(take_L_and_F_set_bits(14), 32767)
        self.assertEqual(take_L_and_F_set_bits(15), 65535)
        self.assertEqual(take_L_and_F_set_bits(16), 131071)
        self.assertEqual(take_L_and_F_set_bits(17), 262143)
        self.assertEqual(take_L_and_F_set_bits(18), 524287)
        self.assertEqual(take_L_and_F_set_bits(19), 1048575)
        self.assertEqual(take_L_and_F_set_bits(20), 2097151)
        self.assertEqual(take_L_and_F_set_bits(21), 4194303)
        self.assertEqual(take_L_and_F_set_bits(22), 8388607)
        self.assertEqual(take_L_and_F_set_bits(23), 16777215)
        self.assertEqual(take_L_and_F_set_bits(24), 33554431)
        self.assertEqual(take_L_and_F_set_bits(25), 67108863)
        self.assertEqual(take_L_and_F_set_bits(26), 134217727)
        self.assertEqual(take_L_and_F_set_bits(27), 268435455)
        self.assertEqual(take_L_and_F_set_bits(28), 536870911)
        self.assertEqual(take_L_and_F_set_bits(29), 1073741823)
        self.assertEqual(take_L_and_F_set_bits(30), 2147483647)
        self.assertEqual(take_L_and_F_set_bits(31), 4294967295)

    def test_toggle_F_and_L_bits(self):
        self.assertEqual(toggle_F_and_L_bits(0),
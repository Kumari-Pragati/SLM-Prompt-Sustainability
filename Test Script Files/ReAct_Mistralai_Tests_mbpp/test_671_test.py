import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_single_bit_set(self):
        self.assertEqual(set_Right_most_Unset_Bit(1), 2)
        self.assertEqual(set_Right_most_Unset_Bit(3), 4)
        self.assertEqual(set_Right_most_Unset_Bit(5), 6)
        self.assertEqual(set_Right_most_Unset_Bit(7), 8)

    def test_multiple_bits_set(self):
        self.assertEqual(set_Right_most_Unset_Bit(9), 16)
        self.assertEqual(set_Right_most_Unset_Bit(10), 17)
        self.assertEqual(set_Right_most_Unset_Bit(11), 18)
        self.assertEqual(set_Right_most_Unset_Bit(12), 19)
        self.assertEqual(set_Right_most_Unset_Bit(13), 20)
        self.assertEqual(set_Right_most_Unset_Bit(14), 28)
        self.assertEqual(set_Right_most_Unset_Bit(15), 32)

    def test_negative_numbers(self):
        self.assertEqual(set_Right_most_Unset_Bit(-1), 0)
        self.assertEqual(set_Right_most_Unset_Bit(-2), 1)
        self.assertEqual(set_Right_most_Unset_Bit(-3), 0)

    def test_max_and_min_int(self):
        self.assertEqual(set_Right_most_Unset_Bit(2**31 - 1), 2**31)
        self.assertEqual(set_Right_most_Unset_Bit(2**31), 0)
        self.assertEqual(set_Right_most_Unset_Bit(-2**31), 2**31)

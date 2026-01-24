import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):

    def test_set_Right_most_Unset_Bit_for_zero(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_set_Right_most_Unset_Bit_for_positive_numbers(self):
        self.assertEqual(set_Right_most_Unset_Bit(1), 1)
        self.assertEqual(set_Right_most_Unset_Bit(2), 2)
        self.assertEqual(set_Right_most_Unset_Bit(3), 3)
        self.assertEqual(set_Right_most_Unset_Bit(4), 4)
        self.assertEqual(set_Right_most_Unset_Bit(5), 5)
        self.assertEqual(set_Right_most_Unset_Bit(6), 6)
        self.assertEqual(set_Right_most_Unset_Bit(7), 7)
        self.assertEqual(set_Right_most_Unset_Bit(8), 8)
        self.assertEqual(set_Right_most_Unset_Bit(9), 9)
        self.assertEqual(set_Right_most_Unset_Bit(10), 10)

    def test_set_Right_most_Unset_Bit_for_negative_numbers(self):
        self.assertEqual(set_Right_most_Unset_Bit(-1), -1)
        self.assertEqual(set_Right_most_Unset_Bit(-2), -2)
        self.assertEqual(set_Right_most_Unset_Bit(-3), -3)
        self.assertEqual(set_Right_most_Unset_Bit(-4), -4)
        self.assertEqual(set_Right_most_Unset_Bit(-5), -5)
        self.assertEqual(set_Right_most_Unset_Bit(-6), -6)
        self.assertEqual(set_Right_most_Unset_Bit(-7), -7)
        self.assertEqual(set_Right_most_Unset_Bit(-8), -8)
        self.assertEqual(set_Right_most_Unset_Bit(-9), -9)
        self.assertEqual(set_Right_most_Unset_Bit(-10), -10)

    def test_set_Right_most_Unset_Bit_for_edge_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(0x00000001), 0x00000001)
        self.assertEqual(set_Right_most_Unset_Bit(0x00000002), 0x00000002)
        self.assertEqual(set_Right_most_Unset_Bit(0x00000004), 0x00000004)
        self.assertEqual(set_Right_most_Unset_Bit(0x00000008), 0x00000008)
        self.assertEqual(set_Right_most_Unset_Bit(0x00000010), 0x00000010)
        self.assertEqual(set_Right_most_Unset_Bit(0x00000020), 0x00000020)
        self.assertEqual(set_Right_most_Unset_Bit(0x00000040), 0x00000040)
        self.assertEqual(set_Right_most_Unset_Bit(0x00000080), 0x00000080)
        self.assertEqual(set_Right_most_Unset_Bit(0x00000100), 0x00000100)
        self.assertEqual(set_Right_most_Unset_Bit(0x00000200), 0x00000200)
        self.assertEqual(set_Right_most_Unset_Bit(0x00000400), 0x00000400)
        self.assertEqual(set_Right_most_Unset_Bit(0x00000800), 0x00000800)
        self.assertEqual(set_Right_most_Unset_Bit(0x00001000), 0x00001000)
        self.assertEqual(set_Right_most_Unset_Bit(0x00002000), 0x00002000)
        self.assertEqual(set_Right_most_Unset_Bit(0x00004000), 0x00004000)
        self.assertEqual(set_Right_most_Unset_Bit(0x00008000), 0x00008000)
        self.assertEqual(set_Right_most_Unset_Bit(0x00010000), 0x00010000)
        self.assertEqual(set_Right_most_Unset_Bit(0x00020000), 0x00020000)
        self.assertEqual(set_Right_most_Unset_Bit(0x00040000), 0x00040000)
        self.assertEqual(set_Right_most_Unset_Bit(0x00080000), 0x00080000)
        self.assertEqual(set_Right_most_Unset_Bit(0x00100000), 0x00100000)
        self.assertEqual(set_Right_most_Unset_Bit(0x00200000), 0x00200000)
        self.assertEqual(set_Right_most_Unset_Bit(0x00400000), 0x00400000)
        self.assertEqual(set_Right_most_Unset_Bit(0x00800000), 0x00800000)
        self.assertEqual(set_Right_most_Unset_Bit(0x01000000), 0x01000000)
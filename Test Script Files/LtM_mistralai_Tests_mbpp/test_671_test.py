import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)
        self.assertEqual(set_Right_most_Unset_Bit(1), 2)
        self.assertEqual(set_Right_most_Unset_Bit(3), 4)
        self.assertEqual(set_Right_most_Unset_Bit(5), 6)

    def test_edge_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(1 << 31), 1 << 31 | 1)
        self.assertEqual(set_Right_most_Unset_Bit(1 << 63), 1)

    def test_complex(self):
        self.assertEqual(set_Right_most_Unset_Bit(0b10101010), 0b10101011)
        self.assertEqual(set_Right_most_Unset_Bit(0b11111111), 0)

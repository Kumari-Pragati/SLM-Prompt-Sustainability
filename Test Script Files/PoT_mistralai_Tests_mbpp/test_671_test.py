import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)
        self.assertEqual(set_Right_most_Unset_Bit(1), 2)
        self.assertEqual(set_Right_most_Unset_Bit(3), 4)
        self.assertEqual(set_Right_most_Unset_Bit(5), 6)
        self.assertEqual(set_Right_most_Unset_Bit(63), 64)
        self.assertEqual(set_Right_most_Unset_Bit(127), 128)
        self.assertEqual(set_Right_most_Unset_Bit(128), 129)
        self.assertEqual(set_Right_most_Unset_Bit(2147483647), 2147483648)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(-1), 0)
        self.assertEqual(set_Right_most_Unset_Bit(0b1000_0000), 0b1000_0001)
        self.assertEqual(set_Right_most_Unset_Bit(0xFFFFFFFF), 0)

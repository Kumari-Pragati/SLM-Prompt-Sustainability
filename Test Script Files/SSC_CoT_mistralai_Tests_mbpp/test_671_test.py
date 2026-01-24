import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)
        self.assertEqual(set_Right_most_Unset_Bit(1), 2)
        self.assertEqual(set_Right_most_Unset_Bit(7), 8)
        self.assertEqual(set_Right_most_Unset_Bit(127), 128)
        self.assertEqual(set_Right_most_Unset_Bit(128), 129)
        self.assertEqual(set_Right_most_Unset_Bit(2147483647), 2147483648)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(set_Right_most_Unset_Bit(-1), 0)
        self.assertEqual(set_Right_most_Unset_Bit(2**32 - 1), 2**32)
        self.assertEqual(set_Right_most_Unset_Bit(2**64 - 1), 2**64)

    def test_special_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(3), 4)
        self.assertEqual(set_Right_most_Unset_Bit(5), 6)
        self.assertEqual(set_Right_most_Unset_Bit(15), 16)
        self.assertEqual(set_Right_most_Unset_Bit(255), 256)
        self.assertEqual(set_Right_most_Unset_Bit(256), 257)
        self.assertEqual(set_Right_most_Unset_Bit(2047), 2048)
        self.assertEqual(set_Right_most_Unset_Bit(2048), 2049)
        self.assertEqual(set_Right_most_Unset_Bit(2097151), 2097152)
        self.assertEqual(set_Right_most_Unset_Bit(2097152), 2097153)

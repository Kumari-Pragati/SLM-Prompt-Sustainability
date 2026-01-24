import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))

    def test_edge_case_min(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 1, 1))

    def test_edge_case_max(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(2**32 - 1, 32, 32))

    def test_edge_case_l_eq_r(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 0, 0))

    def test_edge_case_l_gt_r(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 4))

    def test_error_case_l_lt_0(self):
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 15, -1, 4)

    def test_error_case_r_gt_32(self):
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 15, 4, 33)

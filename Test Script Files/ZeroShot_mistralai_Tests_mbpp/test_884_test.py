import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):

    def test_all_bits_set_in_range(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 3))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 2, 2))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 0, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 0))

    def test_edge_cases(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 0, 0))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 1, 1))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(2147483647, 31, 31))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2147483647, 32, 31))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, -1, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 0, -1))

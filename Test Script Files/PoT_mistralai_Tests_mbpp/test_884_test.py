import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 5, 5))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 6, 6))

    def test_edge_case_start(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 1))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 0))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 4, 4))

    def test_edge_case_end(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 5, 7))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 6, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(31, 5, 5))

    def test_edge_case_range(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 7))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(31, 0, 31))

    def test_corner_case_zero(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 4, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 5, 5))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 6, 6))

    def test_corner_case_negative(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(-1, 4, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(-1, 5, 5))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(-1, 6, 6))

    def test_corner_case_invalid_range(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 7, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 6, 7))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 3))

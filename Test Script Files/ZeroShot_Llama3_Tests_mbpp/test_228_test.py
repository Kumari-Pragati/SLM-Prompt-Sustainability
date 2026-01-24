import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInRange(unittest.TestCase):

    def test_all_Bits_Set_In_The_Given_Range(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 3))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 1, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 3, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 6))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 2, 3))

    def test_edge_cases(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 0, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 1, 1))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 0, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 1, 1))

import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 7))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(255, 8, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(65535, 16, 16))

    def test_edge_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 1, 1))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 1, 1))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 2, 2))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 31, 31))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(2**32 - 1, 32, 32))

    def test_boundary_case(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 1, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 1, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 2, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 32, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2**32, 32, 31))

    def test_invalid_input(self):
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, -1, 1, 1)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 0, 1)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 1, 0)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 32, 33)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 2**32 + 1, 32, 32)

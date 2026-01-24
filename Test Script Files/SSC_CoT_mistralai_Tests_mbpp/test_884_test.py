import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(255, 8, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(65280, 16, 16))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 0, 0))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 1, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 0, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, -1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 1, -1))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(2147483647, 31, 31))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2147483647, 32, 31))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2147483647, 31, 32))

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, -1, 1, 2)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, -1, 2)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 1, -1)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 2, 0)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 0, 0)

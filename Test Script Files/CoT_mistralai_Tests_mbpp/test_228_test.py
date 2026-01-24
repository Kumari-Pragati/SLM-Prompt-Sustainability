import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(255, 8, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 10, 10))

    def test_edge_cases(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 0, 0))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 0, 0))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(3, 0, 1))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 2, 3))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 3, 2))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 3))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 5))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 3))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 2))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 5))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 3))

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, -1, 3, 4)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 0, -1)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, -1, 1)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 1, 0)

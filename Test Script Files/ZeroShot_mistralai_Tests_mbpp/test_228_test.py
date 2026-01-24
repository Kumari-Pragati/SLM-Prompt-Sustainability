import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):

    def test_empty_range(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 0, 0))

    def test_single_bit(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2, 1, 1))

    def test_overlapping_range(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 7))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 6))

    def test_non_overlapping_range(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 9))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 8, 10))

    def test_negative_numbers(self):
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, -1, 1, 2)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, -1, 2)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 1, -1)

    def test_invalid_input(self):
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 1, 0)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 0, 1)

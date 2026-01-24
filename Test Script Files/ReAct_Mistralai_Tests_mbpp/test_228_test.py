import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):

    def test_all_bits_set_in_range(self):
        # Typical case: all bits set in the given range
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 5, 5))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 6, 6))

    def test_bits_not_set_in_range(self):
        # Edge case: no bits set in the given range
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 5, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 5, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2, 5, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(3, 5, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(4, 5, 4))

    def test_bits_set_outside_range(self):
        # Edge case: bits set outside the given range
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 3))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 3))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 6, 3))

    def test_invalid_arguments(self):
        # Error case: invalid arguments
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, -1, 5, 5)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 0, 0, 0)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 6, 6)
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 5, 7)

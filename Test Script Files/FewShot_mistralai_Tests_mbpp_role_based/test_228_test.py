import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):
    def test_all_bits_set_in_range(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 3))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 2, 2))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 5))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 0, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 6, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 6))

    def test_zero_and_negative_values(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 4, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(-1, 4, 4))

    def test_invalid_input_l_greater_than_r(self):
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 15, 6, 4)

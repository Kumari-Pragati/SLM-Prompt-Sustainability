import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(255, 8, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 10, 10))

    def test_edge_case_start_of_range(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 1, 1))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 2, 2))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 3, 3))

    def test_edge_case_end_of_range(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(255, 8, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 10, 10))

    def test_edge_case_overlapping_range(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(16, 3, 5))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(256, 9, 10))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1024, 11, 12))

    def test_edge_case_non_overlapping_range(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(16, 3, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(256, 9, 8))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1024, 11, 10))

    def test_invalid_input_negative_number(self):
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, -1, 3, 4)

    def test_invalid_input_zero(self):
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 0, 3, 4)

    def test_invalid_input_greater_than_pow2(self):
        self.assertRaises(ValueError, all_Bits_Set_In_The_Given_Range, 1, 65, 64)

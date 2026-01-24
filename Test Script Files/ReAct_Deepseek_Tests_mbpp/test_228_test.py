import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInGivenRange(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 3))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(10, 2, 3))

    def test_edge_cases(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 1, 5))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 2, 2))

    def test_explicitly_handled_error_cases(self):
        # Test with negative numbers
        self.assertFalse(all_Bits_Set_In_The_Given_Range(-15, 1, 3))
        # Test with zero
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 1, 3))
        # Test with l > r
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 3, 2))
        # Test with l or r out of range
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 0, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 6))

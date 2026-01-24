import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInGivenRange(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 1, 10))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1023, 1, 9))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 1, 2))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 10, 10))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1023, 10, 9))

    def test_corner_cases(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 1, 10))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1023, 1, 9))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 1, 2))

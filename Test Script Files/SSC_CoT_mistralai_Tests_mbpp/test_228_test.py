import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(31, 5, 5))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(255, 8, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(65535, 16, 16))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(4294967295, 32, 32))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 1, 1))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 1, 1))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 2, 1))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 0, 0))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 0, 1))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 1, 0))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(255, 0, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(65535, 0, 16))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(4294967295, 0, 32))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(4294967295, 32, 33))

    def test_invalid_inputs(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(-1, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 0, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 1, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 2, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 32, 32))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2, 2, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2, 3, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2, 32, 32))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(4294967296, 32, 32))

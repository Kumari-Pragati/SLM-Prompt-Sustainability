import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(31, 5, 5))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(255, 1, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 10, 10))

    def test_edge_and_boundary(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 1, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 2, 2))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 0, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 0))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(16, 4, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(16, 5, 5))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(255, 9, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(255, 8, 8))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1024, 10, 10))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1024, 11, 11))

    def test_complex(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(13, 4, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(13, 5, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(13, 4, 5))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(256, 1, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(256, 9, 8))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1025, 10, 10))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1025, 11, 11))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1025, 10, 12))

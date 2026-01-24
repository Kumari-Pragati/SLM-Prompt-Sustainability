import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(31, 5, 5))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(255, 8, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 10, 10))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(65535, 16, 16))

    def test_edge_and_boundary(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 1, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 2, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(255, 9, 8))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1023, 11, 10))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(65536, 16, 15))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(65536, 17, 16))

    def test_complex(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(10, 4, 5))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(10, 5, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(256, 8, 9))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(256, 9, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1024, 10, 11))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1024, 11, 10))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(65536, 16, 17))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(65536, 17, 16))

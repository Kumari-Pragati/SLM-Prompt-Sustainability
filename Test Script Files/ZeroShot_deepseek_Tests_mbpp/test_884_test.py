import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInGivenRange(unittest.TestCase):

    def test_all_Bits_Set_In_The_Given_Range(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 1, 10))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1023, 1, 9))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 2, 10))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1023, 2, 9))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1023, 3, 10))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1023, 3, 9))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1023, 4, 10))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1023, 4, 9))

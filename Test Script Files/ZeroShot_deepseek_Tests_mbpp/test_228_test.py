import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInGivenRange(unittest.TestCase):

    def test_all_bits_set_in_range_1(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 1, 10))

    def test_all_bits_set_in_range_2(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1023, 1, 9))

    def test_all_bits_set_in_range_3(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 1, 1))

    def test_all_bits_set_in_range_4(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1023, 2, 10))

    def test_all_bits_set_in_range_5(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 10, 10))

    def test_all_bits_set_in_range_6(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 1, 10))

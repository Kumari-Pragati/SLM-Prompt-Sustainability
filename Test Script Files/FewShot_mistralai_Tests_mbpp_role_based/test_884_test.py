import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInTheGivenRange(unittest.TestCase):
    def test_all_bits_set_in_range(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(255, 8, 8))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(65535, 16, 16))

    def test_all_bits_not_set_in_range(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 5, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 4, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2, 4, 3))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(3, 4, 2))

    def test_left_less_than_right(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 5, 4))

    def test_left_equal_right(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 4, 4))

    def test_left_greater_than_right(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2, 4, 3))

    def test_left_zero(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 4, 4))

    def test_left_one(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 4, 4))

    def test_right_zero(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 4, 0))

    def test_right_one(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 4, 1))

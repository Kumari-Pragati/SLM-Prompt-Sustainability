import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSet(unittest.TestCase):
    def test_all_bits_set_in_range(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 3))

    def test_all_bits_set_in_range_with_zero(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 0, 0))

    def test_all_bits_set_in_range_with_negative(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(-1, 0, 3))

    def test_all_bits_set_in_range_with_invalid_l(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range(15, 'a', 3)

    def test_all_bits_set_in_range_with_invalid_r(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range(15, 0, 'b')

    def test_all_bits_set_in_range_with_invalid_n(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range('a', 0, 3)

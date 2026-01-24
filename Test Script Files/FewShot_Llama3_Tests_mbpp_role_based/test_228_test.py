import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSet(unittest.TestCase):
    def test_all_bits_set_in_range(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 3))

    def test_all_bits_set_in_range_with_max_value(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 4))

    def test_no_bits_set_in_range(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(7, 0, 2))

    def test_no_bits_set_in_range_with_max_value(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 0, 4))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range('test', 0, 3)

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            all_Bits_Set_In_The_Given_Range(15, -1, 3)

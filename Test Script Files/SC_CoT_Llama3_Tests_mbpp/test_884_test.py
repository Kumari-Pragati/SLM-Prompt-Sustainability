import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInRange(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 3))

    def test_edge_case_lower_bound(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 3))

    def test_edge_case_upper_bound(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 4))

    def test_edge_case_lower_and_upper_bound(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 0))

    def test_edge_case_range_zero(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 0, 0))

    def test_edge_case_range_negative(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, -1, 0))

    def test_edge_case_range_out_of_range(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 10))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range('15', 0, 3)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range(15, '0', 3)

    def test_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range(15, 0, '3')

    def test_invalid_input_type4(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range(15, 0, [3])

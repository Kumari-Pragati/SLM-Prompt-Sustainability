import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInRange(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 3))

    def test_edge_case_l_equal_r(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 3))

    def test_edge_case_l_greater_than_r(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 3))

    def test_edge_case_l_equal_to_zero(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 0, 0))

    def test_edge_case_r_equal_to_zero(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 0))

    def test_edge_case_l_greater_than_r_and_l_greater_than_31(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 32, 31))

    def test_edge_case_l_greater_than_r_and_l_greater_than_31_and_r_greater_than_31(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 32, 32))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range("15", 0, 3)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range(15, "0", 3)

    def test_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range(15, 0, "3")

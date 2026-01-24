import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInGivenRange(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 3))

    def test_edge_case_l_equals_r(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 3))

    def test_boundary_case_l_greater_than_r(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 3))

    def test_boundary_case_n_is_zero(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 1, 3))

    def test_invalid_input_l_greater_than_32(self):
        with self.assertRaises(ValueError):
            all_Bits_Set_In_The_Given_Range(15, 33, 3)

    def test_invalid_input_r_greater_than_32(self):
        with self.assertRaises(ValueError):
            all_Bits_Set_In_The_Given_Range(15, 1, 33)

    def test_invalid_input_l_less_than_1(self):
        with self.assertRaises(ValueError):
            all_Bits_Set_In_The_Given_Range(15, 0, 3)

    def test_invalid_input_r_less_than_1(self):
        with self.assertRaises(ValueError):
            all_Bits_Set_In_The_Given_Range(15, 1, 0)

import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInGivenRange(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 2, 3))

    def test_edge_case_l_equals_r(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 3))

    def test_edge_case_l_equals_1(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 3))

    def test_edge_case_r_equals_32(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(4294967295, 1, 32))

    def test_invalid_input_l_greater_than_r(self):
        with self.assertRaises(Exception):
            all_Bits_Set_In_The_Given_Range(15, 4, 3)

    def test_invalid_input_l_less_than_1(self):
        with self.assertRaises(Exception):
            all_Bits_Set_In_The_Given_Range(15, 0, 3)

    def test_invalid_input_r_greater_than_32(self):
        with self.assertRaises(Exception):
            all_Bits_Set_In_The_Given_Range(15, 1, 33)

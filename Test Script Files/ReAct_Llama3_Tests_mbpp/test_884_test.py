import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSet(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))

    def test_edge_case_l_equal_r(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 0))

    def test_edge_case_l_greater_than_r(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 8, 4))

    def test_edge_case_l_equal_to_r_plus_one(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 3))

    def test_edge_case_l_greater_than_r_plus_one(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 4))

    def test_edge_case_l_equal_to_r_minus_one(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 2))

    def test_edge_case_l_greater_than_r_minus_one(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 3))

    def test_edge_case_l_equal_to_r(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 4))

    def test_edge_case_l_greater_than_r(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 8, 4))

    def test_edge_case_l_equal_to_r_plus_one(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 3))

    def test_edge_case_l_greater_than_r_plus_one(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 4))

    def test_edge_case_l_equal_to_r_minus_one(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 2))

    def test_edge_case_l_greater_than_r_minus_one(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 3))

    def test_edge_case_l_equal_to_r(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 4))

    def test_edge_case_l_greater_than_r(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 8, 4))

    def test_edge_case_l_equal_to_r_plus_one(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 3))

    def test_edge_case_l_greater_than_r_plus_one(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 4))

    def test_edge_case_l_equal_to_r_minus_one(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 2))

    def test_edge_case_l_greater_than_r_minus_one(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 3))

    def test_edge_case_l_equal_to_r(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 4))

    def test_edge_case_l_greater_than_r(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 8, 4))

    def test_edge_case_l_equal_to_r_plus_one(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 3))

    def test_edge_case_l_greater_than_r_plus_one(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 5, 4))

    def test_edge_case_l_equal_to_r_minus_one(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 2))

    def test_edge_case_l_greater_than_r_minus_one(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 3))

    def test_edge_case_l_equal_to_r(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 4))

    def test_edge_case_l_greater_than_r(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 8, 4))

    def test_edge_case_l_equal_to_r_plus_one(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 3))

    def test_edge_case_l_greater_than_r_plus_one(self
import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInGivenRange(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 3))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(10, 2, 3))

    def test_edge_conditions(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 1, 4))

    def test_boundary_conditions(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(14, 1, 1))

    def test_complex_cases(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(17, 2, 3))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(31, 5, 6))

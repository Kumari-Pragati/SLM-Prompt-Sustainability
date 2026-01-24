import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInGivenRange(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(10, 2, 3))

    def test_edge_conditions(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 1, 2))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 1, 5))

    def test_complex_cases(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(31, 2, 5))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(31, 2, 4))

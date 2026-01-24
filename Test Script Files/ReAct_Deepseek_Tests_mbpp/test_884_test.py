import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInGivenRange(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 3))

    def test_boundary_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 1, 5))

    def test_edge_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 2, 3))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range("15", 1, 3)
        with self.assertRaises(ValueError):
            all_Bits_Set_In_The_Given_Range(15, -1, 3)
        with self.assertRaises(ValueError):
            all_Bits_Set_In_The_Given_Range(15, 1, 0)

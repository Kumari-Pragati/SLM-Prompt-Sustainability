import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInRange(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 3))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(7, 0, 3))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 4))

    def test_edge_cases(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 0, 0))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 0, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 1, 1))

    def test_boundary_cases(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 0, 0))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1, 0, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 1, 1))

    def test_special_cases(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2, 0, 0))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(2, 0, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(2, 1, 1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range('a', 0, 1)
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range(0, 'a', 1)
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range(0, 0, 'a')

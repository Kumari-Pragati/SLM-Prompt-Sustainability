import unittest
from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInRange(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 4, 4))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 4, 3))

    def test_edge_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 1, 0))

    def test_boundary_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(15, 0, 1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range('a', 4, 4)
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range(15, 'a', 4)
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range(15, 4, 'a')

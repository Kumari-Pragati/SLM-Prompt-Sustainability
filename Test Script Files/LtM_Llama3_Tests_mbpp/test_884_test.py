import unittest
from mbpp_884_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInRange(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 3))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 3, 4))
        self.assertTrue(all_Bits_Set_In_The_Given_Range(15, 0, 4))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 0, 0))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 0, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(0, 0, 2))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range('a', 0, 1)
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range(0, 'a', 1)
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range(0, 0, 'a')

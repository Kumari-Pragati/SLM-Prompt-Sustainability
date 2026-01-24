import unittest

from mbpp_228_code import all_Bits_Set_In_The_Given_Range

class TestAllBitsSetInRange(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 1, 10))

    def test_boundary_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(0, 1, 1))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1, 1, 1))

    def test_edge_case(self):
        self.assertTrue(all_Bits_Set_In_The_Given_Range(1023, 10, 10))
        self.assertFalse(all_Bits_Set_In_The_Given_Range(1023, 10, 9))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            all_Bits_Set_In_The_Given_Range("1023", 1, 10)
        with self.assertRaises(ValueError):
            all_Bits_Set_In_The_Given_Range(1023, -1, 10)
        with self.assertRaises(ValueError):
            all_Bits_Set_In_The_Given_Range(1023, 11, 10)

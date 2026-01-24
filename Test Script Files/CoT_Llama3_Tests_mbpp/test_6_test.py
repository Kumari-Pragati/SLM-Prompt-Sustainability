import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):
    def test_power_of_two(self):
        self.assertTrue(differ_At_One_Bit_Pos(8, 4))
        self.assertFalse(differ_At_One_Bit_Pos(5, 3))
        self.assertTrue(differ_At_One_Bit_Pos(16, 8))
        self.assertFalse(differ_At_One_Bit_Pos(10, 2))

    def test_non_power_of_two(self):
        self.assertFalse(differ_At_One_Bit_Pos(9, 3))
        self.assertFalse(differ_At_One_Bit_Pos(15, 7))
        self.assertFalse(differ_At_One_Bit_Pos(20, 12))

    def test_edge_cases(self):
        self.assertFalse(differ_At_One_Bit_Pos(0, 0))
        self.assertFalse(differ_At_One_Bit_Pos(1, 1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos('a', 4)
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos(4, 'b')

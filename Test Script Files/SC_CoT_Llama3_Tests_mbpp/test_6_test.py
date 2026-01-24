import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertTrue(differ_At_One_Bit_Pos(2, 3))
        self.assertTrue(differ_At_One_Bit_Pos(4, 5))
        self.assertFalse(differ_At_One_Bit_Pos(1, 1))

    def test_edge_cases(self):
        self.assertTrue(differ_At_One_Bit_Pos(0, 0))
        self.assertFalse(differ_At_One_Bit_Pos(0, 1))

    def test_power_of_two(self):
        self.assertTrue(differ_At_One_Bit_Pos(2, 2))
        self.assertFalse(differ_At_One_Bit_Pos(3, 3))

    def test_non_power_of_two(self):
        self.assertFalse(differ_At_One_Bit_Pos(2, 4))
        self.assertFalse(differ_At_One_Bit_Pos(3, 5))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos('a', 2)
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos(2, 'b')

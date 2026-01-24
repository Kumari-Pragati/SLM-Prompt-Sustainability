import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertTrue(differ_At_One_Bit_Pos(2, 1))
        self.assertFalse(differ_At_One_Bit_Pos(2, 2))
        self.assertTrue(differ_At_One_Bit_Pos(4, 3))
        self.assertFalse(differ_At_One_Bit_Pos(4, 4))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(differ_At_One_Bit_Pos(0, 0))
        self.assertTrue(differ_At_One_Bit_Pos(1, 0))
        self.assertFalse(differ_At_One_Bit_Pos(2, 2))
        self.assertTrue(differ_At_One_Bit_Pos(4, 4))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos('a', 'b')
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos(None, None)

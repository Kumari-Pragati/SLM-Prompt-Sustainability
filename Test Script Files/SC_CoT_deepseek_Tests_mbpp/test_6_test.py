import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(differ_At_One_Bit_Pos(2, 3))
        self.assertTrue(differ_At_One_Bit_Pos(8, 16))

    def test_boundary_conditions(self):
        self.assertFalse(differ_At_One_Bit_Pos(0, 0))
        self.assertTrue(differ_At_One_Bit_Pos(1, 2))

    def test_edge_cases(self):
        self.assertFalse(differ_At_One_Bit_Pos(255, 256))
        self.assertTrue(differ_At_One_Bit_Pos(2, 1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos("2", 3)
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos(2, "3")
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos("2", "3")

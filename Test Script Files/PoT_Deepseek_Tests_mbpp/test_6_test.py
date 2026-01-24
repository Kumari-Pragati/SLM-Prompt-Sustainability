import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(differ_At_One_Bit_Pos(2, 3))
        self.assertTrue(differ_At_One_Bit_Pos(10, 12))
        self.assertFalse(differ_At_One_Bit_Pos(16, 16))

    def test_edge_cases(self):
        self.assertFalse(differ_At_One_Bit_Pos(0, 0))
        self.assertTrue(differ_At_One_Bit_Pos(0, 1))
        self.assertTrue(differ_At_One_Bit_Pos(255, 0))

    def test_boundary_conditions(self):
        self.assertTrue(differ_At_One_Bit_Pos(2**31 - 1, 2**31))
        self.assertFalse(differ_At_One_Bit_Pos(2**31 - 1, 2**31 - 1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos("10", 12)
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos(10, "12")
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos("10", "12")

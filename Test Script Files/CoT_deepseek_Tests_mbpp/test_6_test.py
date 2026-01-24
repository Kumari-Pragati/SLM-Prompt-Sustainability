import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):

    def test_differ_at_one_bit_pos_typical_case(self):
        self.assertTrue(differ_At_One_Bit_Pos(2, 3))
        self.assertTrue(differ_At_One_Bit_Pos(8, 16))
        self.assertTrue(differ_At_One_Bit_Pos(1, 2))

    def test_differ_at_one_bit_pos_edge_cases(self):
        self.assertFalse(differ_At_One_Bit_Pos(0, 0))
        self.assertFalse(differ_At_One_Bit_Pos(1, 1))
        self.assertFalse(differ_At_One_Bit_Pos(256, 256))

    def test_differ_at_one_bit_pos_boundary_conditions(self):
        self.assertTrue(differ_At_One_Bit_Pos(2**31 - 1, 2**31))
        self.assertTrue(differ_At_One_Bit_Pos(2**32 - 1, 2**32))
        self.assertFalse(differ_At_One_Bit_Pos(2**31, 2**31 - 1))
        self.assertFalse(differ_At_One_Bit_Pos(2**32, 2**32 - 1))

    def test_differ_at_one_bit_pos_invalid_inputs(self):
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos("a", 1)
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos(1, "b")
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos("a", "b")

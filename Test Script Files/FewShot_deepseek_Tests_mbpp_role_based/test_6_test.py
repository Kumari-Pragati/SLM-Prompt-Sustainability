import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):
    def test_differ_at_one_bit_pos_typical_case(self):
        self.assertTrue(differ_At_One_Bit_Pos(2, 3))

    def test_differ_at_one_bit_pos_boundary_conditions(self):
        self.assertFalse(differ_At_One_Bit_Pos(0, 0))
        self.assertFalse(differ_At_One_Bit_Pos(1, 1))

    def test_differ_at_one_bit_pos_edge_cases(self):
        self.assertTrue(differ_At_One_Bit_Pos(2, 10))
        self.assertFalse(differ_At_One_Bit_Pos(8, 16))

    def test_differ_at_one_bit_pos_invalid_inputs(self):
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos("2", 3)
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos(2, "3")

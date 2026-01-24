import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):

    def test_differ_at_one_bit_pos_typical_cases(self):
        self.assertTrue(differ_At_One_Bit_Pos(2, 3))
        self.assertTrue(differ_At_One_Bit_Pos(8, 16))
        self.assertTrue(differ_At_One_Bit_Pos(1, 2))

    def test_differ_at_one_bit_pos_edge_cases(self):
        self.assertFalse(differ_At_One_Bit_Pos(0, 0))
        self.assertFalse(differ_At_One_Bit_Pos(255, 255))
        self.assertTrue(differ_At_One_Bit_Pos(255, 254))

    def test_differ_at_one_bit_pos_error_cases(self):
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos("2", 3)
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos(2, "3")
        with self.assertRaises(TypeError):
            differ_At_One_Bit_Pos("2", "3")

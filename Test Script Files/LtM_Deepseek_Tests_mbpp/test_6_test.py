import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):

    def test_differ_at_one_bit_pos_typical_case(self):
        self.assertTrue(differ_At_One_Bit_Pos(2, 3))
        self.assertTrue(differ_At_One_Bit_Pos(8, 16))
        self.assertFalse(differ_At_One_Bit_Pos(10, 10))

    def test_differ_at_one_bit_pos_edge_cases(self):
        self.assertFalse(differ_At_One_Bit_Pos(0, 0))
        self.assertTrue(differ_At_One_Bit_Pos(1, 2))
        self.assertTrue(differ_At_One_Bit_Pos(255, 0))

    def test_differ_at_one_bit_pos_boundary_conditions(self):
        self.assertTrue(differ_At_One_Bit_Pos(2**31 - 1, 2**31))
        self.assertFalse(differ_At_One_Bit_Pos(2**31, 2**31))

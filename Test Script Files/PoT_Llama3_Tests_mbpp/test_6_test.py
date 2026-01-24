import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(differ_At_One_Bit_Pos(1, 2))
        self.assertTrue(differ_At_One_Bit_Pos(4, 3))
        self.assertFalse(differ_At_One_Bit_Pos(2, 2))
        self.assertFalse(differ_At_One_Bit_Pos(8, 8))

    def test_edge_cases(self):
        self.assertFalse(differ_At_One_Bit_Pos(0, 0))
        self.assertFalse(differ_At_One_Bit_Pos(0, 1))
        self.assertFalse(differ_At_One_Bit_Pos(1, 0))

    def test_power_of_two(self):
        self.assertTrue(differ_At_One_Bit_Pos(2, 1))
        self.assertTrue(differ_At_One_Bit_Pos(4, 2))
        self.assertTrue(differ_At_One_Bit_Pos(8, 4))
        self.assertFalse(differ_At_One_Bit_Pos(2, 4))

    def test_non_power_of_two(self):
        self.assertFalse(differ_At_One_Bit_Pos(3, 2))
        self.assertFalse(differ_At_One_Bit_Pos(5, 3))
        self.assertFalse(differ_At_One_Bit_Pos(6, 4))

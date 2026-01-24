import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):

    def test_differ_At_One_Bit_Pos(self):
        self.assertTrue(differ_At_One_Bit_Pos(2, 3))
        self.assertTrue(differ_At_One_Bit_Pos(8, 4))
        self.assertFalse(differ_At_One_Bit_Pos(16, 16))
        self.assertFalse(differ_At_One_Bit_Pos(0, 0))
        self.assertTrue(differ_At_One_Bit_Pos(1, 2))
        self.assertFalse(differ_At_One_Bit_Pos(10, 12))

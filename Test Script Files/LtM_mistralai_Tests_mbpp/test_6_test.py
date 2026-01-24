import unittest
from mbpp_6_code import differ_At_One_Bit_Pos

class TestDifferAtOneBitPos(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(differ_At_One_Bit_Pos(1, 2), False)
        self.assertEqual(differ_At_One_Bit_Pos(3, 4), False)
        self.assertEqual(differ_At_One_Bit_Pos(5, 10), True)
        self.assertEqual(differ_At_One_Bit_Pos(15, 30), True)

    def test_edge_and_boundary(self):
        self.assertEqual(differ_At_One_Bit_Pos(0, 1), True)
        self.assertEqual(differ_At_One_Bit_Pos(1, 0), True)
        self.assertEqual(differ_At_One_Bit_Pos(1, 1), False)
        self.assertEqual(differ_At_One_Bit_Pos(2**31 - 1, 2**31), True)
        self.assertEqual(differ_At_One_Bit_Pos(2**31, 2**31 - 1), True)

    def test_complex(self):
        self.assertEqual(differ_At_One_Bit_Pos(1 << 15 | 1, 1 << 15 | 2), True)
        self.assertEqual(differ_At_One_Bit_Pos(1 << 15 | 1, 1 << 15 | 1), False)
        self.assertEqual(differ_At_One_Bit_Pos(1 << 15 | 1, 0), True)

import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(get_First_Set_Bit_Pos(5), 2)
        self.assertEqual(get_First_Set_Bit_Pos(10), 3)
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(2), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 1)
        self.assertEqual(get_First_Set_Bit_Pos(127), 7)
        self.assertEqual(get_First_Set_Bit_Pos(2147483647), 31)
        self.assertEqual(get_First_Set_Bit_Pos(-1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(-2), 1)
        self.assertEqual(get_First_Set_Bit_Pos(-2147483648), 32)

    def test_special_cases(self):
        self.assertEqual(get_First_Set_Bit_Pos(2**0), 1)
        self.assertEqual(get_First_Set_Bit_Pos(2**1), 2)
        self.assertEqual(get_First_Set_Bit_Pos(2**31 - 1), 32)
        self.assertEqual(get_First_Set_Bit_Pos(2**31), 32)

import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(get_First_Set_Bit_Pos(3), 1)
        self.assertEqual(get_First_Set_Bit_Pos(5), 2)
        self.assertEqual(get_First_Set_Bit_Pos(24), 4)
        self.assertEqual(get_First_Set_Bit_Pos(255), 8)
        self.assertEqual(get_First_Set_Bit_Pos(2147483647), 31)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 1)
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(2), 1)
        self.assertEqual(get_First_Set_Bit_Pos(2147483648), None)

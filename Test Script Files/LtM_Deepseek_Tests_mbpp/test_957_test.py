import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 0)
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(2), 2)
        self.assertEqual(get_First_Set_Bit_Pos(3), 1)
        self.assertEqual(get_First_Set_Bit_Pos(4), 3)
        self.assertEqual(get_First_Set_Bit_Pos(5), 1)
        self.assertEqual(get_First_Set_Bit_Pos(6), 2)
        self.assertEqual(get_First_Set_Bit_Pos(7), 1)
        self.assertEqual(get_First_Set_Bit_Pos(8), 4)

    def test_edge_conditions(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 0)
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(2**31 - 1), 31)
        self.assertEqual(get_First_Set_Bit_Pos(2**31), 32)

    def test_boundary_conditions(self):
        self.assertEqual(get_First_Set_Bit_Pos(2**31 - 1), 31)
        self.assertEqual(get_First_Set_Bit_Pos(2**31), 32)
        self.assertEqual(get_First_Set_Bit_Pos(2**31 + 1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(2**63 - 1), 63)
        self.assertEqual(get_First_Set_Bit_Pos(2**63), 64)
        self.assertEqual(get_First_Set_Bit_Pos(2**63 + 1), 1)

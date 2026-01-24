import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(2), 1)
        self.assertEqual(get_First_Set_Bit_Pos(3), 2)
        self.assertEqual(get_First_Set_Bit_Pos(4), 2)
        self.assertEqual(get_First_Set_Bit_Pos(5), 2)
        self.assertEqual(get_First_Set_Bit_Pos(6), 3)
        self.assertEqual(get_First_Set_Bit_Pos(7), 3)
        self.assertEqual(get_First_Set_Bit_Pos(8), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 1)
        self.assertEqual(get_First_Set_Bit_Pos(1 << 31), 32)
        self.assertEqual(get_First_Set_Bit_Pos(1 << 63), 64)

    def test_complex_inputs(self):
        self.assertEqual(get_First_Set_Bit_Pos(math.pow(2, 64) - 1), 64)
        self.assertEqual(get_First_Set_Bit_Pos(math.pow(2, 128) - 1), 128)

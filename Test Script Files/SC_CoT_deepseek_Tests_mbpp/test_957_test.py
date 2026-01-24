import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_First_Set_Bit_Pos(18), 2)
        self.assertEqual(get_First_Set_Bit_Pos(32), 5)
        self.assertEqual(get_First_Set_Bit_Pos(64), 7)

    def test_edge_cases(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 0)
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)

    def test_corner_cases(self):
        self.assertEqual(get_First_Set_Bit_Pos(2**31 - 1), 31)
        self.assertEqual(get_First_Set_Bit_Pos(2**63 - 1), 63)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos('18')
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos(18.5)
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos(None)
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos([])

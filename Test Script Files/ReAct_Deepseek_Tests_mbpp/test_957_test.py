import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 0)
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(2), 2)
        self.assertEqual(get_First_Set_Bit_Pos(4), 3)
        self.assertEqual(get_First_Set_Bit_Pos(8), 4)
        self.assertEqual(get_First_Set_Bit_Pos(16), 5)

    def test_edge_cases(self):
        self.assertEqual(get_First_Set_Bit_Pos(31), 5)
        self.assertEqual(get_First_Set_Bit_Pos(32), 6)
        self.assertEqual(get_First_Set_Bit_Pos(63), 6)
        self.assertEqual(get_First_Set_Bit_Pos(64), 7)
        self.assertEqual(get_First_Set_Bit_Pos(127), 7)
        self.assertEqual(get_First_Set_Bit_Pos(128), 8)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos('invalid')
        with self.assertRaises(ValueError):
            get_First_Set_Bit_Pos(-1)

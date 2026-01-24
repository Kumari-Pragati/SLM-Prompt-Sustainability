import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(get_First_Set_Bit_Pos(5), 2)
        self.assertEqual(get_First_Set_Bit_Pos(8), 1)
        self.assertEqual(get_First_Set_Bit_Pos(15), 1)

    def test_edge_cases(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 1)
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(2), 1)
        self.assertEqual(get_First_Set_Bit_Pos(3), 2)
        self.assertEqual(get_First_Set_Bit_Pos(4), 2)

    def test_special_cases(self):
        self.assertEqual(get_First_Set_Bit_Pos(7), 1)
        self.assertEqual(get_First_Set_Bit_Pos(9), 1)
        self.assertEqual(get_First_Set_Bit_Pos(10), 1)
        self.assertEqual(get_First_Set_Bit_Pos(11), 2)
        self.assertEqual(get_First_Set_Bit_Pos(12), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos('a')
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos(None)
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos('')

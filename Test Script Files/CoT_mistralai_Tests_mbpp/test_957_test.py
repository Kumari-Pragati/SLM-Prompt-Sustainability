import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(get_First_Set_Bit_Pos(1), 0)
        self.assertEqual(get_First_Set_Bit_Pos(3), 1)
        self.assertEqual(get_First_Set_Bit_Pos(5), 2)
        self.assertEqual(get_First_Set_Bit_Pos(15), 4)
        self.assertEqual(get_First_Set_Bit_Pos(127), 7)
        self.assertEqual(get_First_Set_Bit_Pos(128), 8)
        self.assertEqual(get_First_Set_Bit_Pos(2147483647), 31)

    def test_zero(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(get_First_Set_Bit_Pos(-1), None)
        self.assertEqual(get_First_Set_Bit_Pos(-2), None)
        self.assertEqual(get_First_Set_Bit_Pos(-3), 0)
        self.assertEqual(get_First_Set_Bit_Pos(-4), 1)
        self.assertEqual(get_First_Set_Bit_Pos(-5), 2)
        self.assertEqual(get_First_Set_Bit_Pos(-127), 7)
        self.assertEqual(get_First_Set_Bit_Pos(-2147483648), 31)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, get_First_Set_Bit_Pos, 'string')
        self.assertRaises(TypeError, get_First_Set_Bit_Pos, 2.5)
        self.assertRaises(TypeError, get_First_Set_Bit_Pos, complex(1, 2))

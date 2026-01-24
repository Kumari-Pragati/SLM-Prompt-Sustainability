import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_First_Set_Bit_Pos(0b1010), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b10000000000000000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b1000000000000000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b100000000000000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b10000000000000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b1000000000000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b100000000000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b10000000000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b1000000000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b100000000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b10000000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b1000000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b100000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b10000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b1000000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b100000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b10000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b1000000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b100000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b10000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b1000000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b100000000000), 1)
        self.assertEqual(get_First_Set_Bit_Pos(0b1000000
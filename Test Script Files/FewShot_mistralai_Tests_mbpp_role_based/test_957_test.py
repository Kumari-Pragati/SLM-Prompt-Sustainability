import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(5), 2)
        self.assertEqual(get_First_Set_Bit_Pos(10), 3)
        self.assertEqual(get_First_Set_Bit_Pos(15), 4)
        self.assertEqual(get_First_Set_Bit_Pos(255), 8)
        self.assertEqual(get_First_Set_Bit_Pos(65535), 16)
        self.assertEqual(get_First_Set_Bit_Pos(2147483647), 31)

    def test_zero(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(get_First_Set_Bit_Pos(-1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(-5), 1)
        self.assertEqual(get_First_Set_Bit_Pos(-10), 1)
        self.assertEqual(get_First_Set_Bit_Pos(-15), 1)
        self.assertEqual(get_First_Set_Bit_Pos(-255), 8)
        self.assertEqual(get_First_Set_Bit_Pos(-65535), 16)
        self.assertEqual(get_First_Set_Bit_Pos(-2147483647), 31)

    def test_one(self):
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)

    def test_powers_of_two(self):
        for i in range(1, 32):
            self.assertEqual(get_First_Set_Bit_Pos(2**i), i)

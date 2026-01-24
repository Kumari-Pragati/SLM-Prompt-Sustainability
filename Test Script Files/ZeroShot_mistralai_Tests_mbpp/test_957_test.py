import unittest
from mbpp_957_code import get_First_Set_Bit_Pos
import math

class TestGetFirstSetBitPos(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 1)

    def test_one(self):
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)

    def test_powers_of_two(self):
        for i in range(1, 32):
            self.assertEqual(get_First_Set_Bit_Pos(2**i), i)

    def test_negative_numbers(self):
        self.assertEqual(get_First_Set_Bit_Pos(-1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(-2), 1)
        self.assertEqual(get_First_Set_Bit_Pos(-3), 2)
        self.assertEqual(get_First_Set_Bit_Pos(-4), 2)
        self.assertEqual(get_First_Set_Bit_Pos(-5), 3)
        self.assertEqual(get_First_Set_Bit_Pos(-6), 3)
        self.assertEqual(get_First_Set_Bit_Pos(-7), 4)
        self.assertEqual(get_First_Set_Bit_Pos(-8), 4)
        self.assertEqual(get_First_Set_Bit_Pos(-9), 5)
        self.assertEqual(get_First_Set_Bit_Pos(-10), 5)
        self.assertEqual(get_First_Set_Bit_Pos(-11), 6)
        self.assertEqual(get_First_Set_Bit_Pos(-12), 6)
        self.assertEqual(get_First_Set_Bit_Pos(-13), 7)
        self.assertEqual(get_First_Set_Bit_Pos(-14), 7)
        self.assertEqual(get_First_Set_Bit_Pos(-15), 8)
        self.assertEqual(get_First_Set_Bit_Pos(-16), 8)
        self.assertEqual(get_First_Set_Bit_Pos(-17), 9)
        self.assertEqual(get_First_Set_Bit_Pos(-18), 9)
        self.assertEqual(get_First_Set_Bit_Pos(-19), 10)
        self.assertEqual(get_First_Set_Bit_Pos(-20), 10)
        self.assertEqual(get_First_Set_Bit_Pos(-21), 11)
        self.assertEqual(get_First_Set_Bit_Pos(-22), 11)
        self.assertEqual(get_First_Set_Bit_Pos(-23), 12)
        self.assertEqual(get_First_Set_Bit_Pos(-24), 12)
        self.assertEqual(get_First_Set_Bit_Pos(-25), 13)
        self.assertEqual(get_First_Set_Bit_Pos(-26), 13)
        self.assertEqual(get_First_Set_Bit_Pos(-27), 14)
        self.assertEqual(get_First_Set_Bit_Pos(-28), 14)
        self.assertEqual(get_First_Set_Bit_Pos(-29), 15)
        self.assertEqual(get_First_Set_Bit_Pos(-30), 15)
        self.assertEqual(get_First_Set_Bit_Pos(-31), 16)
        self.assertEqual(get_First_Set_Bit_Pos(-32), 16)

    def test_random_numbers(self):
        for i in range(100):
            n = math.floor(math.random() * (2**31))
            expected = math.floor(math.log2(n)) + 1
            self.assertEqual(get_First_Set_Bit_Pos(n), expected)

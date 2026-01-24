import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(get_First_Set_Bit_Pos(1), 1)
        self.assertEqual(get_First_Set_Bit_Pos(5), 2)
        self.assertEqual(get_First_Set_Bit_Pos(10), 3)
        self.assertEqual(get_First_Set_Bit_Pos(255), 8)
        self.assertEqual(get_First_Set_Bit_Pos(65535), 16)
        self.assertEqual(get_First_Set_Bit_Pos(2147483647), 31)

    def test_zero(self):
        self.assertIsNone(get_First_Set_Bit_Pos(0))

    def test_negative_numbers(self):
        self.assertIsNone(get_First_Set_Bit_Pos(-1))
        self.assertIsNone(get_First_Set_Bit_Pos(-2))
        self.assertEqual(get_First_Set_Bit_Pos(-3), 1)
        self.assertEqual(get_First_Set_Bit_Pos(-5), 2)
        self.assertEqual(get_First_Set_Bit_Pos(-10), 3)
        self.assertEqual(get_First_Set_Bit_Pos(-2147483648), 32)

    def test_floats(self):
        self.assertEqual(get_First_Set_Bit_Pos(1.0), 0)
        self.assertEqual(get_First_Set_Bit_Pos(2.0), 1)
        self.assertEqual(get_First_Set_Bit_Pos(4.0), 2)
        self.assertEqual(get_First_Set_Bit_Pos(8.0), 3)
        self.assertEqual(get_First_Set_Bit_Pos(16.0), 4)
        self.assertEqual(get_First_Set_Bit_Pos(32.0), 5)

    def test_large_floats(self):
        self.assertEqual(get_First_Set_Bit_Pos(math.pow(2, 53)), 53)
        self.assertEqual(get_First_Set_Bit_Pos(math.pow(2, 54)), 54)
        self.assertEqual(get_First_Set_Bit_Pos(math.pow(2, 55)), 55)
        self.assertEqual(get_First_Set_Bit_Pos(math.pow(2, 56)), 56)
        self.assertEqual(get_First_Set_Bit_Pos(math.pow(2, 57)), 57)
        self.assertEqual(get_First_Set_Bit_Pos(math.pow(2, 58)), 58)

    def test_large_negative_floats(self):
        self.assertEqual(get_First_Set_Bit_Pos(-math.pow(2, 53)), 53)
        self.assertEqual(get_First_Set_Bit_Pos(-math.pow(2, 54)), 54)
        self.assertEqual(get_First_Set_Bit_Pos(-math.pow(2, 55)), 55)
        self.assertEqual(get_First_Set_Bit_Pos(-math.pow(2, 56)), 56)
        self.assertEqual(get_First_Set_Bit_Pos(-math.pow(2, 57)), 57)
        self.assertEqual(get_First_Set_Bit_Pos(-math.pow(2, 58)), 58)

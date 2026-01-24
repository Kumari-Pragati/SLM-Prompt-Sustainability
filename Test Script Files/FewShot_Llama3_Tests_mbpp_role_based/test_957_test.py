import unittest
from mbpp_957_code import get_First_Set_Bit_Pos

class TestGetFirstSetBitPos(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(get_First_Set_Bit_Pos(8), 3)

    def test_power_of_two(self):
        self.assertEqual(get_First_Set_Bit_Pos(16), 4)

    def test_non_power_of_two(self):
        self.assertEqual(get_First_Set_Bit_Pos(10), 2)

    def test_zero(self):
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos(0)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            get_First_Set_Bit_Pos(-8)

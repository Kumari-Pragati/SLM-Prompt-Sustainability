import unittest
from mbpp_957_code import log2

def get_First_Set_Bit_Pos(n):
    return log2(n&-n)+1

class TestGetFirstSetBitPos(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(get_First_Set_Bit_Pos(18), 2)
        self.assertEqual(get_First_Set_Bit_Pos(32), 5)
        self.assertEqual(get_First_Set_Bit_Pos(64), 7)

    def test_negative_numbers(self):
        self.assertEqual(get_First_Set_Bit_Pos(-18), 2)
        self.assertEqual(get_First_Set_Bit_Pos(-32), 5)
        self.assertEqual(get_First_Set_Bit_Pos(-64), 7)

    def test_zero(self):
        self.assertEqual(get_First_Set_Bit_Pos(0), 0)

    def test_large_numbers(self):
        self.assertEqual(get_First_Set_Bit_Pos(1073741824), 30)

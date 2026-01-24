import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(count_Set_Bits(3), 1)
        self.assertEqual(count_Set_Bits(7), 3)
        self.assertEqual(count_Set_Bits(15), 4)

    def test_zero(self):
        self.assertEqual(count_Set_Bits(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_Set_Bits(-1), 1)
        self.assertEqual(count_Set_Bits(-3), 1)
        self.assertEqual(count_Set_Bits(-7), 2)

    def test_large_numbers(self):
        self.assertEqual(count_Set_Bits(1 << 30), 30)
        self.assertEqual(count_Set_Bits(1 << 31), 31)
        self.assertEqual(count_Set_Bits(1 << 63), 64)

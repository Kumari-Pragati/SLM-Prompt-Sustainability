import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(4), 2)
        self.assertEqual(count_Set_Bits(5), 2)
        self.assertEqual(count_Set_Bits(6), 2)
        self.assertEqual(count_Set_Bits(7), 3)
        self.assertEqual(count_Set_Bits(8), 3)
        self.assertEqual(count_Set_Bits(9), 3)
        self.assertEqual(count_Set_Bits(10), 3)

    def test_zero(self):
        self.assertEqual(count_Set_Bits(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_Set_Bits(-1), 1)
        self.assertEqual(count_Set_Bits(-2), 1)
        self.assertEqual(count_Set_Bits(-3), 2)
        self.assertEqual(count_Set_Bits(-4), 2)
        self.assertEqual(count_Set_Bits(-5), 2)
        self.assertEqual(count_Set_Bits(-6), 2)
        self.assertEqual(count_Set_Bits(-7), 3)
        self.assertEqual(count_Set_Bits(-8), 3)
        self.assertEqual(count_Set_Bits(-9), 3)
        self.assertEqual(count_Set_Bits(-10), 3)

    def test_large_numbers(self):
        self.assertEqual(count_Set_Bits(100), 31)
        self.assertEqual(count_Set_Bits(200), 63)
        self.assertEqual(count_Set_Bits(300), 95)
        self.assertEqual(count_Set_Bits(400), 127)
        self.assertEqual(count_Set_Bits(500), 159)

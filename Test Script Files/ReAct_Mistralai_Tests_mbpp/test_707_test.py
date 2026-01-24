import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(count_Set_Bits(0), 0)

    def test_one(self):
        self.assertEqual(count_Set_Bits(1), 1)

    def test_powers_of_two(self):
        for i in range(1, 32):
            self.assertEqual(count_Set_Bits(2**i), i)

    def test_negative_numbers(self):
        self.assertEqual(count_Set_Bits(-1), 31)
        self.assertEqual(count_Set_Bits(-2), 30)
        self.assertEqual(count_Set_Bits(-3), 29)

    def test_large_positive_numbers(self):
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)
        self.assertEqual(count_Set_Bits(2**31), 32)
        self.assertEqual(count_Set_Bits(2**32 - 1), 32)

    def test_large_negative_numbers(self):
        self.assertEqual(count_Set_Bits(-(2**31)), 32)
        self.assertEqual(count_Set_Bits(-(2**31 + 1)), 31)
        self.assertEqual(count_Set_Bits(-(2**32)), 31)

import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_Set_Bits(0), 0)

    def test_one(self):
        self.assertEqual(count_Set_Bits(1), 1)

    def test_positive_numbers(self):
        self.assertEqual(count_Set_Bits(3), 1)
        self.assertEqual(count_Set_Bits(7), 3)
        self.assertEqual(count_Set_Bits(15), 4)

    def test_negative_numbers(self):
        self.assertEqual(count_Set_Bits(-1), 1)
        self.assertEqual(count_Set_Bits(-3), 1)
        self.assertEqual(count_Set_Bits(-7), 2)

    def test_large_numbers(self):
        self.assertEqual(count_Set_Bits(2**16 - 1), 16)
        self.assertEqual(count_Set_Bits(2**32 - 1), 32)

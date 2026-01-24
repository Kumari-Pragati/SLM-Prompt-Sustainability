import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(count_Set_Bits(0), 0)

    def test_one(self):
        self.assertEqual(count_Set_Bits(1), 1)

    def test_negative_numbers(self):
        self.assertEqual(count_Set_Bits(-1), 1)
        self.assertEqual(count_Set_Bits(-2), 1)
        self.assertEqual(count_Set_Bits(-3), 2)

    def test_powers_of_two(self):
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(4), 2)
        self.assertEqual(count_Set_Bits(8), 3)
        self.assertEqual(count_Set_Bits(16), 4)
        self.assertEqual(count_Set_Bits(32), 5)
        self.assertEqual(count_Set_Bits(64), 6)
        self.assertEqual(count_Set_Bits(128), 7)
        self.assertEqual(count_Set_Bits(256), 8)
        self.assertEqual(count_Set_Bits(512), 9)
        self.assertEqual(count_Set_Bits(1024), 10)

    def test_random_numbers(self):
        self.assertEqual(count_Set_Bits(17), 4)
        self.assertEqual(count_Set_Bits(42), 4)
        self.assertEqual(count_Set_Bits(10001), 16)
        self.assertEqual(count_Set_Bits(1000001), 10)

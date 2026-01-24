import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(set_Bit_Number(0), 0)

    def test_one(self):
        self.assertEqual(set_Bit_Number(1), 1 << 0)

    def test_power_of_two(self):
        for i in range(1, 32):
            self.assertEqual(set_Bit_Number(2**i), 1 << i)

    def test_negative_numbers(self):
        self.assertEqual(set_Bit_Number(-1), 0)
        self.assertEqual(set_Bit_Number(-2), 0)

    def test_large_numbers(self):
        self.assertEqual(set_Bit_Number(2**31), 1 << 31)
        self.assertEqual(set_Bit_Number(2**32 - 1), 0)
        self.assertEqual(set_Bit_Number(2**32), 0)

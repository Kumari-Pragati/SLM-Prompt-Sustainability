import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(set_Bit_Number(0), 0)

    def test_one(self):
        self.assertEqual(set_Bit_Number(1), 1 << 0)

    def test_two(self):
        self.assertEqual(set_Bit_Number(2), 1 << 1)

    def test_four(self):
        self.assertEqual(set_Bit_Number(4), 1 << 2)

    def test_eight(self):
        self.assertEqual(set_Bit_Number(8), 1 << 3)

    def test_negative_number(self):
        self.assertRaises(ValueError, set_Bit_Number, -1)

    def test_large_number(self):
        self.assertRaises(ValueError, set_Bit_Number, 2147483648)

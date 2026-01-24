import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(set_Bit_Number(0), 0)

    def test_positive_numbers(self):
        for i in range(1, 32):
            self.assertEqual(set_Bit_Number(i), (1 << i))

    def test_large_number(self):
        self.assertEqual(set_Bit_Number(2147483647), 33)

    def test_negative_numbers(self):
        for i in range(-1, 0):
            self.assertEqual(set_Bit_Number(i), 0)

    def test_invalid_input(self):
        self.assertRaises(ValueError, set_Bit_Number, -2147483648)

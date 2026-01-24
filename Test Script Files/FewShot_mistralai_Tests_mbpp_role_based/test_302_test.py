import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(set_Bit_Number(0), 0)

    def test_power_of_two(self):
        for i in range(1, 33):
            self.assertEqual(set_Bit_Number(2 ** i), 2 ** i)

    def test_negative_number(self):
        self.assertEqual(set_Bit_Number(-1), 0)

    def test_large_number(self):
        self.assertEqual(set_Bit_Number(2 ** 31), 2 ** 31)

    def test_fraction(self):
        self.assertEqual(set_Bit_Number(1.5), 0)

    def test_string(self):
        self.assertEqual(set_Bit_Number('hello'), 0)

import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):
    def test_odd_bit_set_number_positive(self):
        self.assertEqual(odd_bit_set_number(1), 3)
        self.assertEqual(odd_bit_set_number(5), 7)
        self.assertEqual(odd_bit_set_number(9), 15)

    def test_odd_bit_set_number_zero(self):
        self.assertEqual(odd_bit_set_number(0), 1)

    def test_odd_bit_set_number_negative(self):
        self.assertEqual(odd_bit_set_number(-1), -3)
        self.assertEqual(odd_bit_set_number(-5), -7)
        self.assertEqual(odd_bit_set_number(-9), -15)

    def test_odd_bit_set_number_one_bit(self):
        self.assertEqual(odd_bit_set_number(1), 3)
        self.assertEqual(odd_bit_set_number(2), 3)
        self.assertEqual(odd_bit_set_number(4), 5)

    def test_odd_bit_set_number_all_bits(self):
        self.assertEqual(odd_bit_set_number(2**31 - 1), 2**31 - 1)

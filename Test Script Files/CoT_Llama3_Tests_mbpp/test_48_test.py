import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):
    def test_even_number(self):
        self.assertEqual(odd_bit_set_number(4), 4)

    def test_odd_number(self):
        self.assertEqual(odd_bit_set_number(5), 5)

    def test_single_bit_set(self):
        self.assertEqual(odd_bit_set_number(1), 1)

    def test_multiple_bit_set(self):
        self.assertEqual(odd_bit_set_number(15), 15)

    def test_all_bits_set(self):
        self.assertEqual(odd_bit_set_number(15), 15)

    def test_zero_input(self):
        self.assertEqual(odd_bit_set_number(0), 0)

    def test_negative_input(self):
        self.assertEqual(odd_bit_set_number(-5), -5)

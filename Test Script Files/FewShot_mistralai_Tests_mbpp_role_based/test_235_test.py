import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):
    def test_even_bit_set_number_positive(self):
        self.assertEqual(even_bit_set_number(10), 18)
        self.assertEqual(even_bit_set_number(20), 26)
        self.assertEqual(even_bit_set_number(30), 34)

    def test_even_bit_set_number_zero(self):
        self.assertEqual(even_bit_set_number(0), 0)

    def test_even_bit_set_number_negative(self):
        self.assertEqual(even_bit_set_number(-10), 14)
        self.assertEqual(even_bit_set_number(-20), 22)
        self.assertEqual(even_bit_set_number(-30), 26)

    def test_even_bit_set_number_one(self):
        self.assertEqual(even_bit_set_number(1), 1)

    def test_even_bit_set_number_large_positive(self):
        self.assertEqual(even_bit_set_number(2 ** 31 - 1), 2 ** 31 - 1)

    def test_even_bit_set_number_large_negative(self):
        self.assertEqual(even_bit_set_number(-2 ** 31), -2 ** 31)

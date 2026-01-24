import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):

    def test_even_bit_set_number_positive(self):
        self.assertEqual(even_bit_set_number(10), 14)

    def test_even_bit_set_number_negative(self):
        self.assertEqual(even_bit_set_number(-10), -14)

    def test_even_bit_set_number_zero(self):
        self.assertEqual(even_bit_set_number(0), 0)

    def test_even_bit_set_number_single_bit_set(self):
        self.assertEqual(even_bit_set_number(1), 1)

    def test_even_bit_set_number_multiple_bit_set(self):
        self.assertEqual(even_bit_set_number(15), 31)

    def test_even_bit_set_number_all_bits_set(self):
        self.assertEqual(even_bit_set_number(255), 255)

    def test_even_bit_set_number_all_bits_unset(self):
        self.assertEqual(even_bit_set_number(0), 0)

    def test_even_bit_set_number_max_value(self):
        self.assertEqual(even_bit_set_number(2**31 - 1), 2**31 - 1)

    def test_even_bit_set_number_max_value_negative(self):
        self.assertEqual(even_bit_set_number(-(2**31)), -(2**31))

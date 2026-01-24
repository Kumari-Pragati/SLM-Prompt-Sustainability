import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):

    def test_even_bit_set_number_positive(self):
        self.assertEqual(even_bit_set_number(0), 0)
        self.assertEqual(even_bit_set_number(1), 2)
        self.assertEqual(even_bit_set_number(2), 2)
        self.assertEqual(even_bit_set_number(3), 6)
        self.assertEqual(even_bit_set_number(4), 4)
        self.assertEqual(even_bit_set_number(5), 10)
        self.assertEqual(even_bit_set_number(6), 6)
        self.assertEqual(even_bit_set_number(7), 14)
        self.assertEqual(even_bit_set_number(8), 8)
        self.assertEqual(even_bit_set_number(9), 18)
        self.assertEqual(even_bit_set_number(10), 10)
        self.assertEqual(even_bit_set_number(11), 22)
        self.assertEqual(even_bit_set_number(12), 12)
        self.assertEqual(even_bit_set_number(13), 26)
        self.assertEqual(even_bit_set_number(14), 14)
        self.assertEqual(even_bit_set_number(15), 30)

    def test_even_bit_set_number_zero(self):
        self.assertEqual(even_bit_set_number(0), 0)

    def test_even_bit_set_number_negative(self):
        self.assertEqual(even_bit_set_number(-1), 2)
        self.assertEqual(even_bit_set_number(-2), 2)
        self.assertEqual(even_bit_set_number(-3), 6)
        self.assertEqual(even_bit_set_number(-4), 6)
        self.assertEqual(even_bit_set_number(-5), 10)
        self.assertEqual(even_bit_set_number(-6), 6)
        self.assertEqual(even_bit_set_number(-7), 14)
        self.assertEqual(even_bit_set_number(-8), 8)
        self.assertEqual(even_bit_set_number(-9), 14)
        self.assertEqual(even_bit_set_number(-10), 10)
        self.assertEqual(even_bit_set_number(-11), 18)
        self.assertEqual(even_bit_set_number(-12), 12)
        self.assertEqual(even_bit_set_number(-13), 18)
        self.assertEqual(even_bit_set_number(-14), 14)
        self.assertEqual(even_bit_set_number(-15), 22)

    def test_even_bit_set_number_large_positive(self):
        self.assertEqual(even_bit_set_number(2**16), 2**16 | 2)
        self.assertEqual(even_bit_set_number(2**17), 2**17 | 6)
        self.assertEqual(even_bit_set_number(2**18), 2**18 | 10)
        self.assertEqual(even_bit_set_number(2**19), 2**19 | 14)
        self.assertEqual(even_bit_set_number(2**20), 2**20 | 18)
        self.assertEqual(even_bit_set_number(2**21), 2**21 | 22)
        self.assertEqual(even_bit_set_number(2**22), 2**22 | 26)
        self.assertEqual(even_bit_set_number(2**23), 2**23 | 30)
        self.assertEqual(even_bit_set_number(2**24), 2**24 | 34)
        self.assertEqual(even_bit_set_number(2
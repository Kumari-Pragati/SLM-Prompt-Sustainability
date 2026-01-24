import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):

    def test_even_bit_set_number(self):
        self.assertEqual(even_bit_set_number(0), 0)
        self.assertEqual(even_bit_set_number(1), 3)
        self.assertEqual(even_bit_set_number(2), 2)
        self.assertEqual(even_bit_set_number(3), 3)
        self.assertEqual(even_bit_set_number(4), 12)
        self.assertEqual(even_bit_set_number(5), 15)
        self.assertEqual(even_bit_set_number(6), 6)
        self.assertEqual(even_bit_set_number(7), 7)
        self.assertEqual(even_bit_set_number(8), 48)
        self.assertEqual(even_bit_set_number(9), 63)
        self.assertEqual(even_bit_set_number(10), 10)
        self.assertEqual(even_bit_set_number(11), 11)
        self.assertEqual(even_bit_set_number(12), 120)
        self.assertEqual(even_bit_set_number(13), 135)
        self.assertEqual(even_bit_set_number(14), 14)
        self.assertEqual(even_bit_set_number(15), 15)
        self.assertEqual(even_bit_set_number(16), 256)

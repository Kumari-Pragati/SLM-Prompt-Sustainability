import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):

    def test_odd_bit_set_number(self):
        self.assertEqual(odd_bit_set_number(0), 1)
        self.assertEqual(odd_bit_set_number(1), 3)
        self.assertEqual(odd_bit_set_number(2), 3)
        self.assertEqual(odd_bit_set_number(3), 7)
        self.assertEqual(odd_bit_set_number(4), 7)
        self.assertEqual(odd_bit_set_number(5), 15)
        self.assertEqual(odd_bit_set_number(6), 15)
        self.assertEqual(odd_bit_set_number(7), 31)
        self.assertEqual(odd_bit_set_number(8), 31)
        self.assertEqual(odd_bit_set_number(9), 63)
        self.assertEqual(odd_bit_set_number(10), 63)
        self.assertEqual(odd_bit_set_number(11), 127)
        self.assertEqual(odd_bit_set_number(12), 127)
        self.assertEqual(odd_bit_set_number(13), 255)
        self.assertEqual(odd_bit_set_number(14), 255)
        self.assertEqual(odd_bit_set_number(15), 511)
        self.assertEqual(odd_bit_set_number(16), 511)

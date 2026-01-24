import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(odd_bit_set_number(5), 7)
        self.assertEqual(odd_bit_set_number(10), 15)
        self.assertEqual(odd_bit_set_number(21), 27)

    def test_edge_cases(self):
        self.assertEqual(odd_bit_set_number(0), 1)
        self.assertEqual(odd_bit_set_number(1), 3)
        self.assertEqual(odd_bit_set_number(2), 3)
        self.assertEqual(odd_bit_set_number(3), 7)

    def test_negative_number(self):
        self.assertEqual(odd_bit_set_number(-1), 1)
        self.assertEqual(odd_bit_set_number(-2), 3)
        self.assertEqual(odd_bit_set_number(-3), 7)

    def test_large_number(self):
        self.assertEqual(odd_bit_set_number(2**31 - 1), 2**31 - 1)
        self.assertEqual(odd_bit_set_number(2**31), 2**31 + 1)
        self.assertEqual(odd_bit_set_number(2**31 + 1), 2**32 - 1)

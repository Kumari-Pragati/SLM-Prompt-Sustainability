import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_Unset_Bits(0), 1)

    def test_one(self):
        self.assertEqual(count_Unset_Bits(1), 1)

    def test_even_number(self):
        self.assertEqual(count_Unset_Bits(4), 2)

    def test_odd_number(self):
        self.assertEqual(count_Unset_Bits(5), 1)

    def test_large_number(self):
        self.assertEqual(count_Unset_Bits(2147483647), 31)

    def test_negative_number(self):
        self.assertRaises(ValueError, count_Unset_Bits, -1)

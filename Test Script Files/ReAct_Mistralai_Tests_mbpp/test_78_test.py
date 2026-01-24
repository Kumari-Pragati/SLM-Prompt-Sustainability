import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):

    def test_positive_odd_number(self):
        self.assertEqual(count_With_Odd_SetBits(3), 1)

    def test_positive_even_number(self):
        self.assertEqual(count_With_Odd_SetBits(4), 1)

    def test_zero(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)

    def test_negative_number(self):
        self.assertRaises(ValueError, count_With_Odd_SetBits, -1)

    def test_large_positive_number(self):
        self.assertEqual(count_With_Odd_SetBits(2 ** 31 - 1), 2147483647 // 2)

    def test_large_negative_number(self):
        self.assertRaises(ValueError, count_With_Odd_SetBits, -(2 ** 31))

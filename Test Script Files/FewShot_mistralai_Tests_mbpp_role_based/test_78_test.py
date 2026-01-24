import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):
    def test_positive_even_number(self):
        self.assertEqual(count_With_Odd_SetBits(4), 2)

    def test_positive_odd_number(self):
        self.assertEqual(count_With_Odd_SetBits(5), 2)

    def test_zero(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)

    def test_negative_number(self):
        self.assertEqual(count_With_Odd_SetBits(-1), 0)

    def test_large_positive_number(self):
        self.assertEqual(count_With_Odd_SetBits(2 ** 32), 2 ** 31)

    def test_large_negative_number(self):
        self.assertEqual(count_With_Odd_SetBits(-2 ** 32), 2 ** 31)

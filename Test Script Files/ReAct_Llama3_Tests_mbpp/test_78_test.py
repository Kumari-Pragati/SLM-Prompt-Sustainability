import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):

    def test_even(self):
        self.assertEqual(count_With_Odd_SetBits(4), 2)

    def test_odd(self):
        self.assertEqual(count_With_Odd_SetBits(5), 2)

    def test_zero(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)

    def test_one(self):
        self.assertEqual(count_With_Odd_SetBits(1), 0)

    def test_power_of_two(self):
        self.assertEqual(count_With_Odd_SetBits(8), 4)

    def test_power_of_two_plus_one(self):
        self.assertEqual(count_With_Odd_SetBits(9), 5)

    def test_max_int(self):
        self.assertEqual(count_With_Odd_SetBits(2**31 - 1), (2**31 - 1) / 2)

    def test_min_int(self):
        self.assertEqual(count_With_Odd_SetBits(-2**31), (-2**31) / 2)

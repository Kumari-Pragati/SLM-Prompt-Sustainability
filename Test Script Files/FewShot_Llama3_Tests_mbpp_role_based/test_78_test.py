import unittest
from mbpp_78_code import count_With_Odd_SetBits

class TestCountWithOddSetBits(unittest.TestCase):
    def test_even_number(self):
        self.assertEqual(count_With_Odd_SetBits(4), 2)

    def test_odd_number(self):
        self.assertEqual(count_With_Odd_SetBits(5), 2)

    def test_zero(self):
        self.assertEqual(count_With_Odd_SetBits(0), 0)

    def test_negative_number(self):
        self.assertEqual(count_With_Odd_SetBits(-4), 2)

    def test_large_number(self):
        self.assertEqual(count_With_Odd_SetBits(100), 50)

    def test_binary_string(self):
        self.assertEqual(count_With_OddSetBits(0b101010), 5)

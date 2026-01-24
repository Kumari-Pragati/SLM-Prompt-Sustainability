import unittest
from mbpp_845_code import math
from845_code import find_Digits

class TestFindDigits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(find_Digits(0), 0)

    def test_negative_number(self):
        self.assertEqual(find_Digits(-1), 0)

    def test_one(self):
        self.assertEqual(find_Digits(1), 1)

    def test_two(self):
        self.assertEqual(find_Digits(2), 1)

    def test_small_number(self):
        self.assertEqual(find_Digits(3), 1)

    def test_large_number(self):
        self.assertEqual(find_Digits(1000000), 7)

    def test_large_number_with_many_digits(self):
        self.assertEqual(find_Digits(123456789), 9)

    def test_large_number_with_many_zeros(self):
        self.assertEqual(find_Digits(1000000000), 10)

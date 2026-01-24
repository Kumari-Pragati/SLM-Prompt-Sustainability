import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):

    def test_negative_number(self):
        self.assertEqual(find_Digits(-5), 0)

    def test_zero(self):
        self.assertEqual(find_Digits(0), 1)

    def test_single_digit_number(self):
        self.assertEqual(find_Digits(1), 1)

    def test_two_digit_number(self):
        self.assertEqual(find_Digits(10), 2)

    def test_large_number(self):
        self.assertEqual(find_Digits(1000), 4)

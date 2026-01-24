import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):
    def test_positive_zero(self):
        self.assertEqual(find_Digits(0), 1)

    def test_positive_one(self):
        self.assertEqual(find_Digits(1), 1)

    def test_positive_small_number(self):
        self.assertEqual(find_Digits(10), 2)

    def test_positive_large_number(self):
        self.assertEqual(find_Digits(1000000), 7)

    def test_negative_number(self):
        self.assertEqual(find_Digits(-1), 0)

    def test_large_negative_number(self):
        self.assertEqual(find_Digits(-1000000), 0)

import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(find_Digits(0), 0)

    def test_negative(self):
        self.assertEqual(find_Digits(-1), 0)

    def test_one(self):
        self.assertEqual(find_Digits(1), 1)

    def test_small_positive(self):
        self.assertEqual(find_Digits(2), 1)
        self.assertEqual(find_Digits(3), 1)
        self.assertEqual(find_Digits(4), 1)
        self.assertEqual(find_Digits(5), 2)

    def test_large_positive(self):
        self.assertEqual(find_Digits(10), 2)
        self.assertEqual(find_Digits(100), 3)
        self.assertEqual(find_Digits(1000), 4)
        self.assertEqual(find_Digits(10000), 5)

    def test_large_positive_with_leading_zeros(self):
        self.assertEqual(find_Digits(100000), 6)
        self.assertEqual(find_Digits(1000000), 7)
        self.assertEqual(find_Digits(10000000), 8)
        self.assertEqual(find_Digits(100000000), 9)

    def test_large_positive_with_trailing_zeros(self):
        self.assertEqual(find_Digits(10000000000), 10)
        self.assertEqual(find_Digits(100000000000), 11)
        self.assertEqual(find_Digits(1000000000000), 12)
        self.assertEqual(find_Digits(10000000000000), 13)

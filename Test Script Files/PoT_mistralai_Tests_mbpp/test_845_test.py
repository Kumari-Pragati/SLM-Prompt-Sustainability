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
        self.assertEqual(find_Digits(9), 1)
        self.assertEqual(find_Digits(10), 2)
        self.assertEqual(find_Digits(19), 2)
        self.assertEqual(find_Digits(20), 3)

    def test_large_positive(self):
        self.assertEqual(find_Digits(100), 3)
        self.assertEqual(find_Digits(1000), 4)
        self.assertEqual(find_Digits(10000), 5)
        self.assertEqual(find_Digits(100000), 6)
        self.assertEqual(find_Digits(1000000), 7)

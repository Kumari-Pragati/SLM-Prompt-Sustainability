import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(last_Two_Digits(1), 1)
        self.assertEqual(last_Two_Digits(10), 5)
        self.assertEqual(last_Two_Digits(99), 45)

    def test_zero(self):
        self.assertEqual(last_Two_Digits(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(last_Two_Digits(-1), 1)
        self.assertEqual(last_Two_Digits(-10), 5)
        self.assertEqual(last_Two_Digits(-99), 45)

    def test_large_numbers(self):
        self.assertEqual(last_Two_Digits(1000), 0)
        self.assertEqual(last_Two_Digits(10000), 0)
        self.assertEqual(last_Two_Digits(100000), 0)

    def test_small_numbers(self):
        self.assertEqual(last_Two_Digits(1), 1)
        self.assertEqual(last_Two_Digits(2), 2)
        self.assertEqual(last_Two_Digits(3), 3)

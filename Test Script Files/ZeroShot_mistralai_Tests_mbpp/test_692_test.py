import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(last_Two_Digits(0), 0)

    def test_one(self):
        self.assertEqual(last_Two_Digits(1), 1)

    def test_two(self):
        self.assertEqual(last_Two_Digits(2), 2)

    def test_small_numbers(self):
        for i in range(3, 10):
            self.assertEqual(last_Two_Digits(i), i % 10)

    def test_large_numbers(self):
        for i in range(10, 100):
            self.assertEqual(last_Two_Digits(i), (i % 10) * ((i - 1) % 10))

    def test_negative_numbers(self):
        for i in range(-10, 0):
            self.assertEqual(last_Two_Digits(i), last_Two_Digits(-i))

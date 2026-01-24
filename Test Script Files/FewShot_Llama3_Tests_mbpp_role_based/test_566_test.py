import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(sum_digits(1), 1)

    def test_two_digits(self):
        self.assertEqual(sum_digits(12), 3)

    def test_three_digits(self):
        self.assertEqual(sum_digits(123), 6)

    def test_four_digits(self):
        self.assertEqual(sum_digits(1234), 10)

    def test_five_digits(self):
        self.assertEqual(sum_digits(12345), 15)

    def test_zero(self):
        self.assertEqual(sum_digits(0), 0)

    def test_negative_number(self):
        self.assertEqual(sum_digits(-123), 6)

    def test_large_number(self):
        self.assertEqual(sum_digits(123456789), 45)

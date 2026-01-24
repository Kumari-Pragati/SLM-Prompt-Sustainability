import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(sum_digits(123), 6)

    def test_zero(self):
        self.assertEqual(sum_digits(0), 0)

    def test_negative_number(self):
        self.assertEqual(sum_digits(-123), 6)

    def test_large_number(self):
        self.assertEqual(sum_digits(123456789), 45)

    def test_single_digit_number(self):
        self.assertEqual(sum_digits(5), 5)

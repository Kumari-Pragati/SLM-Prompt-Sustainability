import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(sum_digits(0), 0)

    def test_positive_numbers(self):
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(456), 15)
        self.assertEqual(sum_digits(789), 24)

    def test_negative_numbers(self):
        self.assertEqual(sum_digits(-123), 6)
        self.assertEqual(sum_digits(-456), 15)
        self.assertEqual(sum_digits(-789), 24)

    def test_large_numbers(self):
        self.assertEqual(sum_digits(123456789), 45)
        self.assertEqual(sum_digits(987654321), 45)

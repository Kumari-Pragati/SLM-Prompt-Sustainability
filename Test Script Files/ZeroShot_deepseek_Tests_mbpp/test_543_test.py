import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(count_digits(123, 456), 6)
        self.assertEqual(count_digits(100, 200), 3)
        self.assertEqual(count_digits(999, 999), 6)

    def test_negative_numbers(self):
        self.assertEqual(count_digits(-123, -456), 6)
        self.assertEqual(count_digits(-100, -200), 3)
        self.assertEqual(count_digits(-999, -999), 6)

    def test_mixed_numbers(self):
        self.assertEqual(count_digits(-123, 456), 6)
        self.assertEqual(count_digits(-100, 200), 3)
        self.assertEqual(count_digits(999, -999), 6)

    def test_zero(self):
        self.assertEqual(count_digits(0, 0), 1)
        self.assertEqual(count_digits(0, 123), 3)
        self.assertEqual(count_digits(123, 0), 3)

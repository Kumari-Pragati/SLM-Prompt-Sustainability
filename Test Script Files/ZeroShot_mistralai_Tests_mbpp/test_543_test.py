import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(count_digits(0, 0), 1)

    def test_positive_numbers(self):
        self.assertEqual(count_digits(123, 456), 5)

    def test_negative_numbers(self):
        self.assertEqual(count_digits(-123, -456), 5)

    def test_mixed_numbers(self):
        self.assertEqual(count_digits(-123, 456), 5)

    def test_large_numbers(self):
        self.assertEqual(count_digits(123456789, 987654321), 11)

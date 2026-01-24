import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(count_digits(123, 456), 6)

    def test_zero(self):
        self.assertEqual(count_digits(0, 0), 1)

    def test_negative_numbers(self):
        self.assertEqual(count_digits(-123, -456), 6)

    def test_large_numbers(self):
        self.assertEqual(count_digits(123456789, 987654321), 17)

    def test_one_digit_numbers(self):
        self.assertEqual(count_digits(1, 2), 2)

    def test_zero_and_non_zero_numbers(self):
        self.assertEqual(count_digits(0, 123), 4)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            count_digits(0, 0)

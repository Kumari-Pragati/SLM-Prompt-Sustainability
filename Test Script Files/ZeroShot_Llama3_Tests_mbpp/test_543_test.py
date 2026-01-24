import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):

    def test_count_digits_positive(self):
        self.assertEqual(count_digits(123, 456), 3)

    def test_count_digits_negative(self):
        self.assertEqual(count_digits(-123, 456), 3)

    def test_count_digits_zero(self):
        self.assertEqual(count_digits(0, 0), 0)

    def test_count_digits_single_digit(self):
        self.assertEqual(count_digits(1, 2), 1)

    def test_count_digits_large_numbers(self):
        self.assertEqual(count_digits(123456, 789012), 6)

    def test_count_digits_mixed_signs(self):
        self.assertEqual(count_digits(-123, 456), 3)

    def test_count_digits_non_integer(self):
        with self.assertRaises(TypeError):
            count_digits(123.45, 456)

    def test_count_digits_non_numeric(self):
        with self.assertRaises(TypeError):
            count_digits('123', 456)

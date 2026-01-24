import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):

    def test_count_digits_positive_numbers(self):
        self.assertEqual(count_digits(123, 456), 6)
        self.assertEqual(count_digits(987654321, 123456789), 10)

    def test_count_digits_zero(self):
        self.assertEqual(count_digits(0, 0), 1)

    def test_count_digits_negative_numbers(self):
        self.assertEqual(count_digits(-123, -456), 6)
        self.assertEqual(count_digits(-987654321, -123456789), 10)

    def test_count_digits_mixed_numbers(self):
        self.assertEqual(count_digits(123, -456), 6)
        self.assertEqual(count_digits(-123, 456), 6)

    def test_count_digits_large_positive_number(self):
        large_number = 10**20
        self.assertEqual(count_digits(large_number, 0), 20)

    def test_count_digits_large_negative_number(self):
        large_number = -10**20
        self.assertEqual(count_digits(0, large_number), 20)

    def test_count_digits_large_mixed_numbers(self):
        large_number = 10**20
        self.assertEqual(count_digits(large_number, -1), 20)
        self.assertEqual(count_digits(-large_number, 1), 20)

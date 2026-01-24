import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_digits(123, 456), 6)

    def test_single_digit_numbers(self):
        self.assertEqual(count_digits(1, 9), 2)

    def test_zero_numbers(self):
        self.assertEqual(count_digits(0, 0), 1)

    def test_negative_numbers(self):
        self.assertEqual(count_digits(-123, -456), 6)

    def test_large_numbers(self):
        self.assertEqual(count_digits(123456789, 987654321), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_digits("123", 456)

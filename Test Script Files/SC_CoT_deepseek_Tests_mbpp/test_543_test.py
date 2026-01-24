import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_digits(123, 456), 6)

    def test_single_digit_numbers(self):
        self.assertEqual(count_digits(1, 1), 1)
        self.assertEqual(count_digits(0, 0), 1)

    def test_large_numbers(self):
        self.assertEqual(count_digits(1000000, 2000000), 7)

    def test_negative_numbers(self):
        self.assertEqual(count_digits(-123, -456), 6)
        self.assertEqual(count_digits(-123, 456), 6)
        self.assertEqual(count_digits(123, -456), 6)

    def test_zero(self):
        self.assertEqual(count_digits(0, 0), 1)
        self.assertEqual(count_digits(0, 123), 3)
        self.assertEqual(count_digits(123, 0), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_digits("123", 456)
        with self.assertRaises(TypeError):
            count_digits(123, "456")
        with self.assertRaises(TypeError):
            count_digits("123", "456")

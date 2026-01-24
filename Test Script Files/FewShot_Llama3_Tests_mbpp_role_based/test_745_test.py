import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):
    def test_divisible_by_digits_positive_numbers(self):
        self.assertEqual(divisible_by_digits(1, 10), [1, 2, 3, 5, 7, 9])

    def test_divisible_by_digits_negative_numbers(self):
        self.assertEqual(divisible_by_digits(-10, -1), [])

    def test_divisible_by_digits_zero(self):
        self.assertEqual(divisible_by_digits(0, 0), [])

    def test_divisible_by_digits_single_digit(self):
        self.assertEqual(divisible_by_digits(10, 10), [10])

    def test_divisible_by_digits_empty_range(self):
        self.assertEqual(divisible_by_digits(10, 9), [])

    def test_divisible_by_digits_invalid_input(self):
        with self.assertRaises(TypeError):
            divisible_by_digits('a', 10)

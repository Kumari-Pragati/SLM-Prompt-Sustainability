import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_single_digit_numbers(self):
        self.assertEqual(sum_of_digits([1, 2, 3, 4, 5]), 15)

    def test_double_digit_numbers(self):
        self.assertEqual(sum_of_digits([10, 20, 30, 40, 50]), 25)

    def test_mixed_single_and_double_digit_numbers(self):
        self.assertEqual(sum_of_digits([1, 10, 2, 20, 3, 30]), 25)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_digits([-1, -10, -2, -20, -3, -30]), -25)

    def test_with_non_digit_characters(self):
        self.assertEqual(sum_of_digits([123, 456, 789]), 24)

    def test_with_empty_list(self):
        self.assertEqual(sum_of_digits([]), 0)

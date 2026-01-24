import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_digits([123, 456]), 9)
        self.assertEqual(sum_of_digits([12345, 67890]), 55)

    def test_zero(self):
        self.assertEqual(sum_of_digits([0]), 0)
        self.assertEqual(sum_of_digits([0, 0]), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_digits([-123, -456]), 9)
        self.assertEqual(sum_of_digits([-12345, -67890]), 55)

    def test_mixed_numbers(self):
        self.assertEqual(sum_of_digits([123, -456, 7890]), 21)

    def test_empty_list(self):
        self.assertEqual(sum_of_digits([]), 0)

    def test_single_non_numeric_value(self):
        self.assertEqual(sum_of_digits(["a"]), 0)
        self.assertEqual(sum_of_digits(["a", 123]), 123)
        self.assertEqual(sum_of_digits([123, "a"]), 123)

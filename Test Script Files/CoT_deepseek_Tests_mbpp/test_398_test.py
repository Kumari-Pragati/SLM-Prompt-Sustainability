import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_single_digit_numbers(self):
        self.assertEqual(sum_of_digits([1, 2, 3]), 6)
        self.assertEqual(sum_of_digits([4, 5, 6]), 15)

    def test_multiple_digit_numbers(self):
        self.assertEqual(sum_of_digits([12, 34, 56]), 12 + 3 + 4 + 5 + 6)
        self.assertEqual(sum_of_digits([78, 90, 12]), 7 + 8 + 9 + 0 + 1 + 2)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_digits([-12, -34, -56]), 12 + 3 + 4 + 5 + 6)
        self.assertEqual(sum_of_digits([-78, -90, -12]), 7 + 8 + 9 + 0 + 1 + 2)

    def test_mixed_numbers(self):
        self.assertEqual(sum_of_digits([12, -34, 56]), 12 + 3 + 4 + 5 + 6)
        self.assertEqual(sum_of_digits([-78, 90, -12]), 7 + 8 + 9 + 0 + 1 + 2)

    def test_empty_list(self):
        self.assertEqual(sum_of_digits([]), 0)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            sum_of_digits([12, '34', 56])

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            sum_of_digits([12, None, 56])

import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(sum_of_digits([1]), 1)

    def test_multiple_digits(self):
        self.assertEqual(sum_of_digits([12, 34, 56]), 122)

    def test_zero(self):
        self.assertEqual(sum_of_digits([0]), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_digits([-1, -2, -3]), -6)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sum_of_digits(['a', 'b', 'c'])

    def test_empty_input(self):
        self.assertEqual(sum_of_digits([]), 0)

    def test_mixed_input(self):
        self.assertEqual(sum_of_digits([1, '2', 3.5, 4]), 10)

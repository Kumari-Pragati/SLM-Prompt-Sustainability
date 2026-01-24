import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_simple_numbers(self):
        self.assertEqual(sum_of_digits([123, 456]), 18)
        self.assertEqual(sum_of_digits([789, 101]), 18)

    def test_single_digit_numbers(self):
        self.assertEqual(sum_of_digits([1, 2, 3]), 6)
        self.assertEqual(sum_of_digits([4, 5, 6]), 15)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_digits([-123, -456]), -18)
        self.assertEqual(sum_of_digits([-789, -101]), -18)

    def test_numbers_with_leading_zeros(self):
        self.assertEqual(sum_of_digits([123, 045, 067]), 18)

    def test_empty_list(self):
        self.assertEqual(sum_of_digits([]), 0)

    def test_large_numbers(self):
        self.assertEqual(sum_of_digits([987654321, 123456789]), 45)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            sum_of_digits([123, '456', 789])

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            sum_of_digits([123.4, 567.8])

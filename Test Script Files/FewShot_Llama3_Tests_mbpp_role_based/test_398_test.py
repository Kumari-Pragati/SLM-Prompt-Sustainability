import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_single_digit_number(self):
        self.assertEqual(sum_of_digits([1]), 1)

    def test_multiple_digit_number(self):
        self.assertEqual(sum_of_digits([123]), 6)

    def test_multiple_numbers(self):
        self.assertEqual(sum_of_digits([123, 456, 789]), 21)

    def test_empty_list(self):
        self.assertEqual(sum_of_digits([]), 0)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            sum_of_digits(['a', 'b', 'c'])

    def test_mixed_integer_and_non_integer_input(self):
        with self.assertRaises(TypeError):
            sum_of_digits([1, 'a', 3, 'b'])

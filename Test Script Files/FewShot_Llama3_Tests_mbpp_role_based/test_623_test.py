import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(nth_nums([1, 2, 3, 4, 5], 2), [1, 4, 9, 16, 25])

    def test_negative_numbers(self):
        self.assertEqual(nth_nums([-1, -2, -3, -4, -5], 2), [1, 4, 9, 16, 25])

    def test_zero(self):
        self.assertEqual(nth_nums([1, 2, 3, 4, 5], 0), [1, 1, 1, 1, 1])

    def test_non_integer_power(self):
        self.assertEqual(nth_nums([1, 2, 3, 4, 5], 0.5), [1.0, 1.4142135623730951, 2.8284271247461903, 4.0, 5.0])

    def test_empty_list(self):
        self.assertEqual(nth_nums([], 2), [])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            nth_nums('hello', 2)

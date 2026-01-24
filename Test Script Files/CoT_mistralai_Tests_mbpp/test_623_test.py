import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(nth_nums([], 2), [])

    def test_single_element(self):
        self.assertListEqual(nth_nums([1], 2), [1])

    def test_positive_numbers(self):
        self.assertListEqual(nth_nums([1, 2, 3, 4, 5], 2), [1, 4, 9, 16, 25])

    def test_negative_numbers(self):
        self.assertListEqual(nth_nums([-1, -2, -3, -4, -5], 2), [1, 4, 9, 16, 25])

    def test_floats(self):
        self.assertListEqual(nth_nums([1.5, 2.5, 3.5, 4.5, 5.5], 2), [2.25, 6.25, 10.88, 16.88, 27.64])

    def test_zero_base(self):
        self.assertListEqual(nth_nums([1, 2, 3, 4, 5], 0), [1, 1, 1, 1, 1])

    def test_zero_exponent(self):
        self.assertListEqual(nth_nums([1, 2, 3, 4, 5], 0), [1, 1, 1, 1, 1])

    def test_negative_exponent(self):
        self.assertListEqual(nth_nums([1, 2, 3, 4, 5], -2), [1, 4, 9, 16, 25])

    def test_invalid_input_empty_exponent(self):
        with self.assertRaises(ValueError):
            nth_nums([], '')

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(TypeError):
            nth_nums(['a', 'b', 'c'], 2)

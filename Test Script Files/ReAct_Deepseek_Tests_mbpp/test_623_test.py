import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(nth_nums([1, 2, 3], 2), [1, 4, 9])

    def test_negative_numbers(self):
        self.assertEqual(nth_nums([-1, -2, -3], 2), [1, 4, 9])

    def test_zero(self):
        self.assertEqual(nth_nums([0], 2), [0])

    def test_large_numbers(self):
        self.assertEqual(nth_nums([100, 200, 300], 3), [1000000, 800000000, 270000000000])

    def test_zero_power(self):
        self.assertEqual(nth_nums([1, 2, 3], 0), [1, 1, 1])

    def test_negative_power(self):
        self.assertEqual(nth_nums([1, 2, 3], -1), [1, 0.5, 0.3333333333333333])

    def test_empty_list(self):
        self.assertEqual(nth_nums([], 2), [])

    def test_invalid_power(self):
        with self.assertRaises(TypeError):
            nth_nums([1, 2, 3], 'a')

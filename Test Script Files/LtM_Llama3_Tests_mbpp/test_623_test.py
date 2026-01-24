import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(nth_nums([1, 2, 3], 2), [1, 4, 9])

    def test_empty_input(self):
        self.assertEqual(nth_nums([], 2), [])

    def test_single_element_input(self):
        self.assertEqual(nth_nums([5], 2), [25])

    def test_negative_power(self):
        self.assertEqual(nth_nums([1, 2, 3], -2), [1, 1/4, 1/9])

    def test_zero_power(self):
        self.assertEqual(nth_nums([1, 2, 3], 0), [1, 2, 3])

    def test_negative_input(self):
        self.assertEqual(nth_nums([-1, -2, -3], 2), [1, 4, 9])

    def test_mixed_input(self):
        self.assertEqual(nth_nums([-1, 2, 3], 2), [1, 4, 9])

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
        self.assertEqual(nth_nums([100, 200, 300], 2), [10000, 40000, 90000])

    def test_large_exponent(self):
        self.assertEqual(nth_nums([2, 3, 4], 10), [1024, 59049, 1048576])

    def test_empty_list(self):
        self.assertEqual(nth_nums([], 2), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            nth_nums("invalid", 2)

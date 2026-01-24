import unittest
from mbpp_865_code import ntimes_list

class TestNtimesList(unittest.TestCase):

    def test_empty_input(self):
        self.assertListEqual(ntimes_list([], 3), [])

    def test_single_input(self):
        self.assertListEqual(ntimes_list([1], 3), [3])

    def test_positive_numbers(self):
        self.assertListEqual(ntimes_list([1, 2, 3], 4), [4, 8, 12])

    def test_negative_numbers(self):
        self.assertListEqual(ntimes_list([-1, -2, -3], 4), [-4, -8, -12])

    def test_floats(self):
        self.assertListEqual(ntimes_list([1.5, 2.5], 3), [4.5, 7.5])

    def test_zero_multiplier(self):
        self.assertListEqual(ntimes_list([1, 2, 3], 0), [0, 0, 0])

    def test_negative_multiplier(self):
        self.assertListEqual(ntimes_list([1, 2, 3], -2), [-2, -4, -6])

    def test_large_multiplier(self):
        self.assertListEqual(ntimes_list([1, 2, 3], 100), [100, 200, 300])

    def test_large_numbers(self):
        self.assertListEqual(ntimes_list([1000000, 2000000, 3000000], 10),
                             [10000000, 20000000, 30000000])

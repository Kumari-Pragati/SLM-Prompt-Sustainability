import unittest
from mbpp_865_code import ntimes_list

class TestNtimesList(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(ntimes_list([1, 2, 3], 2), [2, 4, 6])

    def test_zero_multiplier(self):
        self.assertEqual(ntimes_list([1, 2, 3], 0), [0, 0, 0])

    def test_negative_multiplier(self):
        self.assertEqual(ntimes_list([-1, -2, -3], -2), [2, 4, 6])

    def test_empty_nums(self):
        self.assertEqual(ntimes_list([], 3), [])

    def test_single_number(self):
        self.assertEqual(ntimes_list([4], 2), [8])

    def test_negative_numbers(self):
        self.assertEqual(ntimes_list([-1, -2], 3), [-3, -6])

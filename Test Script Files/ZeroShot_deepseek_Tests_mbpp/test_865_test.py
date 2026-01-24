import unittest
from mbpp_865_code import ntimes_list

class TestNtimesList(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(ntimes_list([1, 2, 3], 2), [2, 4, 6])

    def test_negative_numbers(self):
        self.assertEqual(ntimes_list([-1, -2, -3], 2), [-2, -4, -6])

    def test_mixed_numbers(self):
        self.assertEqual(ntimes_list([1, -2, 3], 2), [2, -4, 6])

    def test_zero(self):
        self.assertEqual(ntimes_list([0, 2, 3], 2), [0, 4, 6])

    def test_empty_list(self):
        self.assertEqual(ntimes_list([], 2), [])

    def test_large_numbers(self):
        self.assertEqual(ntimes_list([1000000, 2000000, 3000000], 2), [2000000, 4000000, 6000000])

import unittest
from mbpp_865_code import ntimes_list

class TestNtimesList(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(ntimes_list([], 3), [])

    def test_single_element(self):
        self.assertListEqual(ntimes_list([1], 3), [3])

    def test_multiple_elements(self):
        self.assertListEqual(ntimes_list([1, 2, 3], 2), [2, 4, 6])

    def test_negative_numbers(self):
        self.assertListEqual(ntimes_list([-1, -2, -3], 2), [-2, -4, -6])

    def test_zero_multiplier(self):
        self.assertListEqual(ntimes_list([1, 2, 3], 0), [])

    def test_zero_numbers(self):
        self.assertListEqual(ntimes_list([0, 0, 0], 2), [0, 0, 0])

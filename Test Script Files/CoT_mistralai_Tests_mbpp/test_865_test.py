import unittest
from mbpp_865_code import ntimes_list

class TestNtimesList(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(ntimes_list([], 3), [])

    def test_single_element(self):
        self.assertListEqual(ntimes_list([1], 2), [2])

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

    def test_invalid_multiplier(self):
        self.assertRaises(TypeError, ntimes_list, [1, 2, 3], 'not_a_number')

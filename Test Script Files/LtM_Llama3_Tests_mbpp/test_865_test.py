import unittest
from mbpp_865_code import ntimes_list

class TestNtimesList(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(ntimes_list([1, 2, 3], 2), [2, 4, 6])

    def test_empty_input(self):
        self.assertEqual(ntimes_list([], 2), [])

    def test_single_element_input(self):
        self.assertEqual(ntimes_list([5], 3), [15])

    def test_negative_input(self):
        self.assertEqual(ntimes_list([-1, -2, -3], 2), [-2, -4, -6])

    def test_zero_input(self):
        self.assertEqual(ntimes_list([0, 0, 0], 2), [0, 0, 0])

    def test_non_integer_input(self):
        self.assertEqual(ntimes_list([1.5, 2.5, 3.5], 2), [3, 5, 7])

    def test_non_integer_multiplier(self):
        self.assertEqual(ntimes_list([1, 2, 3], 2.5), [2.5, 5, 7.5])

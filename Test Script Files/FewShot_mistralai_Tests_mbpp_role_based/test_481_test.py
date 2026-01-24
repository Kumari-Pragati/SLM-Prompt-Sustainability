import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):
    def test_empty_set(self):
        self.assertFalse(is_subset_sum([], 0, 0))

    def test_empty_sum(self):
        self.assertTrue(is_subset_sum([1, 2, 3], 0, 0))

    def test_single_element_set(self):
        self.assertTrue(is_subset_sum([1], 1, 1))
        self.assertFalse(is_subset_sum([1], 2, 1))

    def test_sum_greater_than_set_sum(self):
        self.assertFalse(is_subset_sum([1, 2, 3], 4, 6))

    def test_negative_numbers(self):
        self.assertFalse(is_subset_sum([-1, -2, -3], 0, 0))

    def test_negative_sum(self):
        self.assertFalse(is_subset_sum([1, 2, 3], -1, 0))

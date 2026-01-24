import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):
    def test_empty_set(self):
        self.assertFalse(is_subset_sum([], 1, 1))

    def test_empty_sum(self):
        self.assertTrue(is_subset_sum([1], 1, 1))

    def test_single_element(self):
        self.assertTrue(is_subset_sum([1], 1, 1))
        self.assertFalse(is_subset_sum([1], 2, 1))

    def test_multiple_elements(self):
        self.assertTrue(is_subset_sum([1, 2], 3, 3))
        self.assertFalse(is_subset_sum([1, 2], 4, 3))
        self.assertTrue(is_subset_sum([1, 2], 2, 2))

    def test_negative_numbers(self):
        self.assertTrue(is_subset_sum([-1, 2], 1, -1))

    def test_large_numbers(self):
        self.assertTrue(is_subset_sum([1, 2, 3, 4, 5], 9, 9))

    def test_sum_greater_than_set_sum(self):
        self.assertFalse(is_subset_sum([1, 2, 3], 4, 6))

    def test_negative_sum(self):
        self.assertRaises(ValueError, is_subset_sum, [1, 2, 3], 1, -1)

    def test_empty_set_and_sum(self):
        self.assertRaises(ValueError, is_subset_sum, [], 1, 1)

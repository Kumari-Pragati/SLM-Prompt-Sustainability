import unittest
from481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):
    def test_empty_set(self):
        self.assertFalse(is_subset_sum([], 0, 0))

    def test_empty_sum(self):
        self.assertTrue(is_subset_sum([1], 1, 1))
        self.assertFalse(is_subset_sum([1], 1, 2))

    def test_single_element(self):
        self.assertTrue(is_subset_sum([1], 1, 1))
        self.assertFalse(is_subset_sum([1], 1, 2))

    def test_sum_greater_than_set(self):
        self.assertFalse(is_subset_sum([1, 2], 1, 3))

    def test_negative_numbers(self):
        self.assertTrue(is_subset_sum([-1, 2], 1, 1))

    def test_duplicate_numbers(self):
        self.assertTrue(is_subset_sum([1, 1], 1, 1))
        self.assertFalse(is_subset_sum([1, 1], 1, 2))

    def test_large_numbers(self):
        self.assertTrue(is_subset_sum([1, 2, 3, 4, 5], 4, 9))
        self.assertFalse(is_subset_sum([1, 2, 3, 4, 5], 4, 10))

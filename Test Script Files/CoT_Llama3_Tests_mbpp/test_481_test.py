import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):
    def test_subset_sum_true(self):
        self.assertTrue(is_subset_sum([1, 2, 3, 4, 5], 5, 7))

    def test_subset_sum_false(self):
        self.assertFalse(is_subset_sum([1, 2, 3, 4, 5], 5, 10))

    def test_subset_sum_zero(self):
        self.assertTrue(is_subset_sum([1, 2, 3, 4, 5], 5, 0))

    def test_subset_sum_single_element(self):
        self.assertTrue(is_subset_sum([1], 1, 1))

    def test_subset_sum_empty_set(self):
        self.assertFalse(is_subset_sum([], 0, 5))

    def test_subset_sum_empty_set_with_sum_zero(self):
        self.assertTrue(is_subset_sum([], 0, 0))

    def test_subset_sum_negative_sum(self):
        self.assertFalse(is_subset_sum([1, 2, 3, 4, 5], 5, -5))

    def test_subset_sum_negative_sum_with_zero(self):
        self.assertTrue(is_subset_sum([1, 2, 3, 4, 5], 5, 0))

import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):

    def test_is_subset_sum_true(self):
        self.assertTrue(is_subset_sum([3, 34, 4, 12, 5, 2], 6, 9))

    def test_is_subset_sum_false(self):
        self.assertFalse(is_subset_sum([3, 34, 4, 12, 5, 2], 6, 10))

    def test_is_subset_sum_zero(self):
        self.assertTrue(is_subset_sum([3, 34, 4, 12, 5, 2], 6, 0))

    def test_is_subset_sum_zero_false(self):
        self.assertFalse(is_subset_sum([3, 34, 4, 12, 5, 2], 6, 1))

    def test_is_subset_sum_negative(self):
        self.assertFalse(is_subset_sum([3, 34, 4, 12, 5, 2], 6, -1))

    def test_is_subset_sum_empty_set(self):
        self.assertFalse(is_subset_sum([], 0, 10))

    def test_is_subset_sum_single_element(self):
        self.assertFalse(is_subset_sum([5], 1, 10))

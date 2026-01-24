import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):

    def test_simple_true(self):
        self.assertTrue(is_subset_sum([1, 2, 3], 3, 3))

    def test_simple_false(self):
        self.assertFalse(is_subset_sum([1, 2, 3], 3, 4))

    def test_empty_set(self):
        self.assertFalse(is_subset_sum([], 1, 1))

    def test_empty_sum(self):
        self.assertTrue(is_subset_sum([1], 0))

    def test_sum_greater_than_set(self):
        self.assertFalse(is_subset_sum([1, 2, 3], 5, 4))

    def test_negative_numbers(self):
        self.assertTrue(is_subset_sum([-1, -2, -3], 1, -1))

    def test_duplicate_numbers(self):
        self.assertTrue(is_subset_sum([1, 1, 2, 3], 4, 4))

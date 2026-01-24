import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):
    def test_empty_set(self):
        self.assertFalse(is_subset_sum([], 0, 10))

    def test_single_element_set(self):
        self.assertTrue(is_subset_sum([10], 1, 10))
        self.assertFalse(is_subset_sum([10], 1, 11))

    def test_multiple_elements_set(self):
        self.assertTrue(is_subset_sum([1, 2, 3], 3, 6))
        self.assertFalse(is_subset_sum([1, 2, 3], 3, 7))

    def test_zero_sum(self):
        self.assertTrue(is_subset_sum([1, 2, 3], 3, 0))

    def test_zero_set(self):
        self.assertFalse(is_subset_sum([], 0, 0))

    def test_negative_sum(self):
        self.assertFalse(is_subset_sum([1, 2, 3], 3, -1))

    def test_negative_set(self):
        self.assertFalse(is_subset_sum([-1, -2, -3], 3, 0))

import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):

    def test_empty_set(self):
        self.assertFalse(is_subset_sum([], 0, 10))

    def test_single_element_set(self):
        self.assertTrue(is_subset_sum([5], 1, 5))
        self.assertFalse(is_subset_sum([5], 1, 6))

    def test_multiple_elements_set(self):
        self.assertTrue(is_subset_sum([3, 34, 4, 12, 5, 2], 6, 9))
        self.assertFalse(is_subset_sum([3, 34, 4, 12, 5, 2], 6, 30))

    def test_large_set(self):
        large_set = list(range(1, 1001))
        self.assertTrue(is_subset_sum(large_set, 1000, 500500))
        self.assertFalse(is_subset_sum(large_set, 1000, 1001001))

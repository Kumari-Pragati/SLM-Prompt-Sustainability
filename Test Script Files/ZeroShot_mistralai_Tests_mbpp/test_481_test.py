import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):

    def test_empty_set(self):
        self.assertFalse(is_subset_sum([], 1, 1))

    def test_single_element(self):
        self.assertFalse(is_subset_sum([1], 2, 1))
        self.assertTrue(is_subset_sum([1], 1, 1))

    def test_multiple_elements(self):
        self.assertTrue(is_subset_sum([1, 2, 3], 4, 4))
        self.assertTrue(is_subset_sum([1, 2, 3], 5, 6))
        self.assertFalse(is_subset_sum([1, 2, 3], 6, 5))
        self.assertFalse(is_subset_sum([1, 2, 3], 7, 4))

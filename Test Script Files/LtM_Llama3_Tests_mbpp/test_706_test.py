import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):
    def test_empty_inputs(self):
        self.assertTrue(is_subset([], 0, [], 0))
        self.assertFalse(is_subset([1], 1, [], 0))
        self.assertFalse(is_subset([], 0, [1], 1))

    def test_single_element_inputs(self):
        self.assertTrue(is_subset([1], 1, [1], 1))
        self.assertFalse(is_subset([1], 1, [2], 1))
        self.assertFalse(is_subset([1, 2], 2, [1], 1))

    def test_subset_inputs(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2], 2))
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 3], 2))
        self.assertTrue(is_subset([1, 2, 3], 3, [2, 3], 2))

    def test_non_subset_inputs(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [4, 5], 2))
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 4], 2))
        self.assertFalse(is_subset([1, 2, 3], 3, [2, 4], 2))

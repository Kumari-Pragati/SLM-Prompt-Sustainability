import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):
    def test_empty_arrays(self):
        self.assertTrue(is_subset([], 0, [], 0))
        self.assertFalse(is_subset([], 1, [], 0))
        self.assertFalse(is_subset([], 0, [1], 1))
        self.assertTrue(is_subset([], 0, [1], 0))

    def test_single_element_arrays(self):
        self.assertTrue(is_subset([1], 1, [1], 1))
        self.assertFalse(is_subset([1], 1, [2], 1))
        self.assertFalse(is_subset([1], 1, [1, 2], 2))
        self.assertTrue(is_subset([1], 1, [1], 0))

    def test_arrays_with_duplicates(self):
        self.assertTrue(is_subset([1, 1], 2, [1], 1))
        self.assertTrue(is_subset([1], 1, [1, 1], 2))
        self.assertFalse(is_subset([1, 2], 2, [1], 1))
        self.assertFalse(is_subset([1], 1, [1, 2], 2))

    def test_arrays_with_different_lengths(self):
        self.assertFalse(is_subset([1, 2], 2, [1], 1))
        self.assertFalse(is_subset([1], 1, [1, 2], 2))
        self.assertTrue(is_subset([1, 2], 2, [1], 1))
        self.assertTrue(is_subset([1], 1, [1, 2], 2))

    def test_arrays_with_overlapping_elements(self):
        self.assertTrue(is_subset([1, 2], 2, [2, 1], 2))
        self.assertTrue(is_subset([2, 1], 2, [1, 2], 2))
        self.assertFalse(is_subset([1, 2], 2, [3], 1))
        self.assertFalse(is_subset([3], 1, [1, 2], 2))

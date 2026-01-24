import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):

    def test_empty_arrays(self):
        self.assertTrue(is_subset([], 0, [], 0))

    def test_single_element_arrays(self):
        self.assertTrue(is_subset([1], 1, [], 0))
        self.assertFalse(is_subset([], 0, [1], 1))

    def test_identical_arrays(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2, 3], 3))

    def test_subset_arrays(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2], 2))
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2, 3, 4], 4))

    def test_non_subset_arrays(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [4, 5, 6], 3))
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 4], 3))

    def test_negative_array_length(self):
        self.assertRaises(IndexError, is_subset, [1, 2, 3], -1, [4, 5, 6], 3)
        self.assertRaises(IndexError, is_subset, [1, 2, 3], 3, [-1, -2, -3], -1)

    def test_empty_set(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 3], 3, set()))

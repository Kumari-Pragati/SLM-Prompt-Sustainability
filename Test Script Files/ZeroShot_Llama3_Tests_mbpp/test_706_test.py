import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):

    def test_is_subset_true(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2, 3, 4, 5], 5))

    def test_is_subset_false(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 3, 4, 5, 6], 6))

    def test_is_subset_empty_array(self):
        self.assertTrue(is_subset([], 0, [], 0))

    def test_is_subset_single_element(self):
        self.assertTrue(is_subset([1], 1, [1, 2, 3], 3))

    def test_is_subset_empty_array2(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [], 0))

    def test_is_subset_single_element2(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [1], 1))

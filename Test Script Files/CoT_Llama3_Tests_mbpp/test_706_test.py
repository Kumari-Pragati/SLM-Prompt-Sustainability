import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):

    def test_subset_true(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2, 3], 3))

    def test_subset_false(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 4], 4))

    def test_subset_empty(self):
        self.assertTrue(is_subset([], 0, [], 0))

    def test_subset_single_element(self):
        self.assertTrue(is_subset([1], 1, [1], 1))

    def test_subset_subset_of_subset(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2], 2))

    def test_subset_subset_of_subset_with_duplicates(self):
        self.assertTrue(is_subset([1, 2, 2, 3], 4, [1, 2, 2], 3))

    def test_subset_subset_with_duplicates(self):
        self.assertTrue(is_subset([1, 2, 2, 3], 4, [1, 2, 2, 3], 4))

    def test_subset_subset_with_duplicates_and_empty(self):
        self.assertTrue(is_subset([1, 2, 2, 3], 4, [1, 2, 2], 3))

    def test_subset_subset_with_duplicates_and_empty_subset(self):
        self.assertTrue(is_subset([1, 2, 2, 3], 4, [], 0))

    def test_subset_subset_with_duplicates_and_empty_subset2(self):
        self.assertFalse(is_subset([1, 2, 2, 3], 4, [1, 2, 3], 3))

    def test_subset_subset_with_duplicates_and_empty_subset3(self):
        self.assertFalse(is_subset([1, 2, 2, 3], 4, [1, 2, 3, 4], 4))

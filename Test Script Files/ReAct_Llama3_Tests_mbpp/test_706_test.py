import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):
    def test_empty_set(self):
        self.assertTrue(is_subset([], 0, [], 0))

    def test_subset(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2, 3], 3))

    def test_superset(self):
        self.assertFalse(is_subset([1, 2, 3, 4, 5], 5, [1, 2, 3], 3))

    def test_not_subset(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 4], 3))

    def test_empty_set_superset(self):
        self.assertFalse(is_subset([], 0, [1, 2, 3], 3))

    def test_empty_set_subset(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [], 0))

    def test_single_element(self):
        self.assertTrue(is_subset([1], 1, [1], 1))

    def test_single_element_not_subset(self):
        self.assertFalse(is_subset([1], 1, [2], 1))

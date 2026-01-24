import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):

    def test_empty_arrays(self):
        self.assertTrue(is_subset([], 0, [], 0))

    def test_subset(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2], 2))

    def test_not_subset(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 4], 3))

    def test_duplicate_elements(self):
        self.assertTrue(is_subset([1, 2, 2], 3, [2], 1))
        self.assertFalse(is_subset([1, 2, 2], 3, [2, 3], 2))

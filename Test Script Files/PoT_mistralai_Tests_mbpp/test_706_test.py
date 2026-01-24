import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2, 3, 4], 4))
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2, 3], 3))
        self.assertTrue(is_subset([], 0, [1, 2, 3], 3))
        self.assertTrue(is_subset([1, 2, 3], 3, [], 0))

    def test_edge_cases(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 3, 4], 5))
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 3, 4], -1))
        self.assertFalse(is_subset([1, 2, 3], -1, [1, 2, 3], 3))
        self.assertFalse(is_subset([], 0, [1, 2, 3], -1))
        self.assertFalse(is_subset([1, 2, 3], -1, [], 0))

    def test_corner_cases(self):
        self.assertTrue(is_subset([], 0, [], 0))
        self.assertTrue(is_subset([1], 1, [], 0))
        self.assertFalse(is_subset([1], 1, [1], 0))
        self.assertTrue(is_subset([1, 1], 2, [1], 1))
        self.assertFalse(is_subset([1, 2], 2, [2, 1], 2))

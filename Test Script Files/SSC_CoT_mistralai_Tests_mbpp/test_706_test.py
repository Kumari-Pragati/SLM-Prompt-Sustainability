import unittest
from mbpp_706_code import sentinel

from706_code import is_subset

class TestIsSubset(unittest.TestCase):

    def test_is_subset_typical_input(self):
        self.assertTrue(is_subset([1, 2, 3], len([1, 2, 3]), [1, 2], len([1, 2])))
        self.assertTrue(is_subset([4, 5, 6], len([4, 5, 6]), [4, 5], len([4, 5])))

    def test_is_subset_edge_input(self):
        self.assertFalse(is_subset([], 0, [1], 1))
        self.assertFalse(is_subset([1], 1, [], 0))
        self.assertFalse(is_subset([1, 2], 2, [1, 3], 2))
        self.assertFalse(is_subset([1, 2], 2, [1, 2, 3], 3))
        self.assertFalse(is_subset([1, 2], 2, [1, 2, 3], 4))

    def test_is_subset_empty_subsets(self):
        self.assertTrue(is_subset([], 0, [], 0))
        self.assertTrue(is_subset([], 0, [sentinel.empty_set], 0))
        self.assertTrue(is_subset([sentinel.empty_set], 1, [], 0))

    def test_is_subset_invalid_inputs(self):
        self.assertRaises(TypeError, is_subset, 1, 2, "a", "b")
        self.assertRaises(TypeError, is_subset, [1], 2.5, [2], 2)

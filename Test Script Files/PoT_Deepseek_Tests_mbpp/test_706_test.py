import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [2, 3, 4], 3))
        self.assertFalse(is_subset([1, 2, 3], 3, [2, 4, 6], 3))

    def test_edge_cases(self):
        self.assertTrue(is_subset([], 0, [], 0))
        self.assertFalse(is_subset([1], 1, [], 0))

    def test_boundary_conditions(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2, 3], 3))
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2], 2))

    def test_corner_cases(self):
        self.assertTrue(is_subset([1, 1, 1], 3, [1, 1], 2))
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 3, 4], 4))

import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2, 3], 3))
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 4], 3))

    def test_empty_inputs(self):
        self.assertTrue(is_subset([], 0, [], 0))
        self.assertFalse(is_subset([1], 1, [], 0))

    def test_edge_conditions(self):
        self.assertTrue(is_subset([1], 1, [1], 1))
        self.assertFalse(is_subset([1], 1, [2], 1))

    def test_complex_cases(self):
        self.assertTrue(is_subset([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5], 5))
        self.assertFalse(is_subset([1, 2, 3, 4, 5], 5, [1, 2, 3, 4], 4))

import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):
    def test_normal(self):
        self.assertTrue(is_subset_sum([3, 7, 4, 8], 10, [3, 7, 4]))
        self.assertTrue(is_subset_sum([2, 3, 5, 6], 10, [2, 3, 5, 6, 1]))

    def test_edge_cases(self):
        self.assertFalse(is_subset_sum([], 5, [1, 2, 3]))
        self.assertFalse(is_subset_sum([1], 0, [1, 2, 3]))
        self.assertFalse(is_subset_sum([1, 2], 3, [1, 2, 3]))
        self.assertFalse(is_subset_sum([1, 2], 4, [1, 2, 3]))
        self.assertFalse(is_subset_sum([1, 2], 5, [1, 2, 3, 4]))

    def test_boundary_cases(self):
        self.assertTrue(is_subset_sum([1], 1, [1]))
        self.assertTrue(is_subset_sum([1, 2], 3, [1, 2]))
        self.assertTrue(is_subset_sum([1, 2], 2, [1, 2]))
        self.assertFalse(is_subset_sum([1, 2], 0, [1, 2]))
        self.assertFalse(is_subset_sum([1, 2], 4, [1, 2]))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_subset_sum, [1, 2], '5', [1, 2])
        self.assertRaises(TypeError, is_subset_sum, [1, 2], 5, '1, 2')

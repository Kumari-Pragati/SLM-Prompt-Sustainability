import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_subset_sum([3, 34, 4, 12, 5, 2], 6, 9))
        self.assertFalse(is_subset_sum([3, 34, 4, 12, 5, 2], 6, 30))

    def test_edge_cases(self):
        self.assertTrue(is_subset_sum([], 0, 0))
        self.assertFalse(is_subset_sum([1], 1, 0))

    def test_boundary_conditions(self):
        self.assertTrue(is_subset_sum([1], 1, 1))
        self.assertFalse(is_subset_sum([1], 1, 2))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_subset_sum("not a list", 1, 1)
        with self.assertRaises(TypeError):
            is_subset_sum([1, 2, 3], "not an integer", 6)
        with self.assertRaises(TypeError):
            is_subset_sum([1, 2, 3], 1, "not an integer")

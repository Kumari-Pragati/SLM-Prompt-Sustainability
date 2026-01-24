import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2, 3], 3))

    def test_edge_case_empty_set(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [], 0))

    def test_edge_case_empty_array(self):
        self.assertTrue(is_subset([], 0, [], 0))

    def test_edge_case_single_element(self):
        self.assertTrue(is_subset([1], 1, [1], 1))

    def test_edge_case_subset(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2], 2))

    def test_edge_case_superset(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 3, 4], 4))

    def test_edge_case_disjoint(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [4, 5, 6], 3))

    def test_edge_case_subset_with_duplicates(self):
        self.assertTrue(is_subset([1, 2, 2, 3], 4, [1, 2, 3], 3))

    def test_edge_case_superset_with_duplicates(self):
        self.assertFalse(is_subset([1, 2, 2, 3], 4, [1, 2, 3, 4, 4], 5))

    def test_edge_case_disjoint_with_duplicates(self):
        self.assertFalse(is_subset([1, 2, 2, 3], 4, [4, 5, 5, 6], 4))

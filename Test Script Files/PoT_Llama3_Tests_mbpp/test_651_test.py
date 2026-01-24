import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2)))
    def test_edge_case_subset(self):
        self.assertTrue(check_subset((1, 2, 3, 4), (1, 2, 3)))
    def test_edge_case_superset(self):
        self.assertTrue(check_subset((1, 2, 3, 4), (1, 2, 3, 4)))
    def test_edge_case_empty_subset(self):
        self.assertTrue(check_subset((), ()))
    def test_edge_case_empty_superset(self):
        self.assertTrue(check_subset((), (1, 2)))
    def test_edge_case_subset_with_duplicates(self):
        self.assertTrue(check_subset((1, 2, 2, 3), (1, 2)))
    def test_edge_case_superset_with_duplicates(self):
        self.assertTrue(check_subset((1, 2, 2, 3, 4), (1, 2, 2, 3)))
    def test_edge_case_subset_with_duplicates_and_empty(self):
        self.assertTrue(check_subset((1, 2, 2, 3), ()))
    def test_edge_case_superset_with_duplicates_and_empty(self):
        self.assertTrue(check_subset((1, 2, 2, 3, 4), ()))
    def test_edge_case_subset_with_duplicates_and_empty_subset(self):
        self.assertTrue(check_subset((1, 2, 2, 3), (1, 2)))
    def test_edge_case_superset_with_duplicates_and_empty_superset(self):
        self.assertTrue(check_subset((1, 2, 2, 3, 4), (1, 2, 2, 3)))

import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2]))

    def test_edge_case_empty_list(self):
        self.assertFalse(check_subset_list([], [1, 2]))

    def test_edge_case_single_element_list(self):
        self.assertTrue(check_subset_list([1], [1]))

    def test_edge_case_subset_list(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2]))

    def test_edge_case_superset_list(self):
        self.assertFalse(check_subset_list([1, 2, 3], [1, 2, 3, 4]))

    def test_edge_case_subset_list_with_duplicates(self):
        self.assertTrue(check_subset_list([1, 2, 2, 3], [1, 2]))

    def test_edge_case_superset_list_with_duplicates(self):
        self.assertFalse(check_subset_list([1, 2, 2, 3], [1, 2, 3, 4]))

    def test_edge_case_subset_list_with_duplicates_and_order_matters(self):
        self.assertFalse(check_subset_list([1, 2, 3], [2, 1]))

    def test_edge_case_superset_list_with_duplicates_and_order_matters(self):
        self.assertFalse(check_subset_list([1, 2, 2, 3], [1, 2, 3, 4]))

    def test_edge_case_subset_list_with_duplicates_and_order_matters_and_empty_list(self):
        self.assertFalse(check_subset_list([], [1, 2]))

    def test_edge_case_superset_list_with_duplicates_and_order_matters_and_empty_list(self):
        self.assertFalse(check_subset_list([1, 2, 2, 3], [1, 2, 3, 4]))

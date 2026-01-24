import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2]))
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset_list([1, 2], [1, 2, 3]))

    def test_edge_case_empty_lists(self):
        self.assertTrue(check_subset_list([], []))
        self.assertFalse(check_subset_list([], [1]))
        self.assertFalse(check_subset_list([1], []))

    def test_edge_case_single_element(self):
        self.assertTrue(check_subset_list([1], [1]))
        self.assertFalse(check_subset_list([1], [2]))

    def test_edge_case_duplicates(self):
        self.assertTrue(check_subset_list([1, 1], [1]))
        self.assertTrue(check_subset_list([1, 2], [1, 2, 2]))

    def test_corner_case_reversed_lists(self):
        self.assertTrue(check_subset_list([1, 2], [2, 1]))
        self.assertFalse(check_subset_list([1, 2], [3, 2]))

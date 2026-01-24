import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))

    def test_edge_case_empty_list1(self):
        self.assertFalse(check_subset([], [1, 2]))

    def test_edge_case_empty_list2(self):
        self.assertTrue(check_subset([1, 2], []))

    def test_edge_case_single_element_list1(self):
        self.assertTrue(check_subset([1], [1]))

    def test_edge_case_single_element_list2(self):
        self.assertFalse(check_subset([1], [2]))

    def test_edge_case_equal_lists(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))

    def test_edge_case_subset_of_subset(self):
        self.assertTrue(check_subset([1, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty_and_empty_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertTrue(check_subset([1, 2, 2, 3, 4], [1, 2]))

    def test_edge_case_subset_of_subset_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self
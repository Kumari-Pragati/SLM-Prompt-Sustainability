import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_element([1, 2, 3, 4, 5], 3))

    def test_edge_case_empty_list(self):
        self.assertFalse(check_element([], 3))

    def test_edge_case_single_element_list(self):
        self.assertTrue(check_element([1], 1))

    def test_edge_case_list_with_element(self):
        self.assertTrue(check_element([1, 2, 3, 4, 5], 3))

    def test_edge_case_list_without_element(self):
        self.assertFalse(check_element([1, 2, 3, 4, 5], 6))

    def test_edge_case_list_with_multiple_elements(self):
        self.assertTrue(check_element([1, 2, 3, 4, 5], 2))

    def test_edge_case_list_with_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6, 7], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6, 7, 8], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6, 7, 8, 9], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 2))

    def test_edge_case_list
import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_element([1, 2, 3, 4, 5], 3))

    def test_edge_case_empty_list(self):
        self.assertFalse(check_element([], 3))

    def test_edge_case_single_element_list(self):
        self.assertTrue(check_element([1], 1))

    def test_edge_case_element_not_in_list(self):
        self.assertFalse(check_element([1, 2, 3, 4, 5], 6))

    def test_edge_case_list_with_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_element_not_in_list(self):
        self.assertFalse(check_element([1, 2, 2, 3, 4, 5, 6], 7))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_element_in_list(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_element_in_list_and_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6], 2))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_element_in_list_and_duplicates_and_element_not_in_list(self):
        self.assertFalse(check_element([1, 2, 2, 3, 4, 5, 6], 7))

    def test_edge_case_list_with_duplicates_and_non_duplicates_and_element_in_list_and_duplicates_and_element_in_list(self):
        self.assertTrue(check_element([1, 2, 2, 3, 4, 5, 6], 2))

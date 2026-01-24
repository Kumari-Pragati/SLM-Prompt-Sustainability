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
        self.assertTrue(check_element([1, 2, 3], 2))

    def test_edge_case_list_without_element(self):
        self.assertFalse(check_element([1, 2, 3], 4))

    def test_edge_case_list_with_duplicates(self):
        self.assertTrue(check_element([1, 2, 2, 3], 2))

    def test_edge_case_list_with_duplicates_and_element(self):
        self.assertTrue(check_element([1, 2, 2, 3], 2))

    def test_edge_case_list_with_duplicates_and_no_element(self):
        self.assertFalse(check_element([1, 2, 2, 3], 4))

    def test_edge_case_list_with_duplicates_and_element_at_end(self):
        self.assertTrue(check_element([1, 2, 2, 3], 3))

    def test_edge_case_list_with_duplicates_and_element_at_start(self):
        self.assertTrue(check_element([1, 2, 2, 3], 1))

    def test_edge_case_list_with_duplicates_and_element_in_middle(self):
        self.assertTrue(check_element([1, 2, 2, 3], 2))

    def test_edge_case_list_with_duplicates_and_element_at_start_and_end(self):
        self.assertTrue(check_element([1, 2, 2, 3], 1))

    def test_edge_case_list_with_duplicates_and_element_at_start_and_middle(self):
        self.assertTrue(check_element([1, 2, 2, 3], 1))

    def test_edge_case_list_with_duplicates_and_element_at_start_and_end_and_middle(self):
        self.assertTrue(check_element([1, 2, 2, 3], 1))

    def test_edge_case_list_with_duplicates_and_element_at_start_and_end_and_middle_and_end(self):
        self.assertTrue(check_element([1, 2, 2, 3], 1))

    def test_edge_case_list_with_duplicates_and_element_at_start_and_end_and_middle_and_start(self):
        self.assertTrue(check_element([1, 2, 2, 3], 1))

    def test_edge_case_list_with_duplicates_and_element_at_start_and_end_and_middle_and_start_and_end(self):
        self.assertTrue(check_element([1, 2, 2, 3], 1))

    def test_edge_case_list_with_duplicates_and_element_at_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertTrue(check_element([1, 2, 2, 3], 1))

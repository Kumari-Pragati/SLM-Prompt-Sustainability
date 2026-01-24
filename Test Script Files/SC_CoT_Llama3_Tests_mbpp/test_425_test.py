import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 2), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_element_in_list([], 1), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(count_element_in_list([1], 1), 1)

    def test_edge_case_list_with_single_element(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 5), 1)

    def test_edge_case_list_with_multiple_elements(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5, 2, 3], 2), 2)

    def test_edge_case_list_with_multiple_elements_and_duplicates(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 3, 3, 4, 5, 5, 5], 3), 3)

    def test_edge_case_list_with_multiple_elements_and_duplicates_and_non_duplicates(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6], 3), 3)

    def test_edge_case_list_with_multiple_elements_and_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7], 3), 3)

    def test_edge_case_list_with_multiple_elements_and_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8], 3), 3)

    def test_edge_case_list_with_multiple_elements_and_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9], 3), 3)

    def test_edge_case_list_with_multiple_elements_and_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10], 3), 3)

    def test_edge_case_list_with_multiple_elements_and_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 11], 3), 3)

    def test_edge_case_list_with_multiple_elements_and_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12], 3), 3)

    def test_edge_case_list_with_multiple_elements_and_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13], 3), 3)

    def test_edge_case_list_with_multiple_elements_and_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates_and_non_duplicates(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 3), 3)

    def test
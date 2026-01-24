import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 3]), [1])

    def test_edge_case_equal_lists(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1]), [1, 1, 1])

    def test_edge_case_empty_lists(self):
        self.assertEqual(extract_index_list([], [], []), [])

    def test_edge_case_single_element_lists(self):
        self.assertEqual(extract_index_list([1], [1], [1]), [1])

    def test_edge_case_single_element_lists_with_duplicates(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1]), [1, 1, 1])

    def test_edge_case_single_element_lists_with_duplicates_and_empty(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1], [1, 1, 1]), [1, 1])

    def test_edge_case_single_element_lists_with_duplicates_and_empty_and_empty(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], []), [1, 1])

    def test_edge_case_single_element_lists_with_duplicates_and_empty_and_empty_and_empty(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1]), [1, 1, 1])

    def test_edge_case_single_element_lists_with_duplicates_and_empty_and_empty_and_empty_and_empty(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1, 1]), [1, 1, 1])

    def test_edge_case_single_element_lists_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1]), [1, 1, 1])

    def test_edge_case_single_element_lists_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]), [1, 1, 1])

    def test_edge_case_single_element_lists_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1]), [1, 1, 1])

    def test_edge_case_single_element_lists_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]), [1, 1, 1])

    def test_edge_case_single_element_lists_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]), [1, 1, 1])

    def test_edge_case_single_element_lists_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [1, 1, 1])

    def test_edge_case_single_element_lists_with_duplicates_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty_and_empty(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1,
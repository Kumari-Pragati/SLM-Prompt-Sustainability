import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 3), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_element_in_list([], 5), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(count_element_in_list([5], 5), 1)

    def test_edge_case_single_element_list_non_matching(self):
        self.assertEqual(count_element_in_list([5], 3), 0)

    def test_edge_case_list_with_single_element(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 1), 1)

    def test_edge_case_list_with_multiple_elements(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 2), 1)

    def test_edge_case_list_with_multiple_elements_non_matching(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 6), 0)

    def test_edge_case_list_with_multiple_elements_and_duplicates(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 4, 5], 2), 2)

    def test_edge_case_list_with_multiple_elements_and_duplicates_non_matching(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 4, 5], 6), 0)

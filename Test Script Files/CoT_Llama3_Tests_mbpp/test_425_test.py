import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 3), 1)

    def test_multiple_occurrences(self):
        self.assertEqual(count_element_in_list([1, 2, 2, 3, 4, 5], 2), 2)

    def test_no_occurrences(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 6), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_element_in_list([], 1), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(count_element_in_list([1], 1), 1)

    def test_edge_case_single_element_list_no_match(self):
        self.assertEqual(count_element_in_list([1], 2), 0)

    def test_edge_case_single_element_list_match(self):
        self.assertEqual(count_element_in_list([1], 1), 1)

    def test_edge_case_single_element_list_match_at_end(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 5), 1)

    def test_edge_case_single_element_list_match_at_start(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 1), 1)

    def test_edge_case_single_element_list_match_at_middle(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 3), 1)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            count_element_in_list(123, 1)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            count_element_in_list([1, 2, 3], 'a')

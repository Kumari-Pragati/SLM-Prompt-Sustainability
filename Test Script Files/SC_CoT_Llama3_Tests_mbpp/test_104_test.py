import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_input(self):
        input_list = [[1, 2], [3, 4], [5, 6]]
        expected_output = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_edge_case_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_edge_case_single_element_list(self):
        input_list = [[1, 2]]
        expected_output = [[1, 2]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_edge_case_single_element_list_empty(self):
        input_list = [[]]
        expected_output = [[]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_edge_case_sublist_empty(self):
        input_list = [[], [1, 2], [3, 4]]
        expected_output = [[], [1, 2], [3, 4]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_edge_case_sublist_single_element(self):
        input_list = [[], [1, 2], [3, 4]]
        expected_output = [[], [1, 2], [3, 4]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sort_sublists('Invalid Input')

    def test_invalid_input_non_list_of_lists(self):
        with self.assertRaises(TypeError):
            sort_sublists([1, 2, 3])

    def test_invalid_input_non_list_of_lists_of_lists(self):
        with self.assertRaises(TypeError):
            sort_sublists([[1, 2], 3, 4])

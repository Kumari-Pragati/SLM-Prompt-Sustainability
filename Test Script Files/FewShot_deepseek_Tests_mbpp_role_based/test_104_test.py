import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_typical_use_case(self):
        input_list = [[3, 2, 1], [6, 5, 4]]
        expected_output = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_edge_case_empty_sublist(self):
        input_list = [[]]
        expected_output = [[]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_boundary_case_single_element_sublist(self):
        input_list = [[5]]
        expected_output = [[5]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_error_handling_non_list_input(self):
        with self.assertRaises(TypeError):
            sort_sublists(104)

    def test_error_handling_non_list_in_list_input(self):
        with self.assertRaises(TypeError):
            sort_sublists([1, 2, 3])

    def test_error_handling_non_integer_in_sublist(self):
        input_list = [[1, 2, '3']]
        with self.assertRaises(TypeError):
            sort_sublists(input_list)

import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        input_list = [[3, 4, 1, 2], [5, 6, 7, 8]]
        expected_output = [[1, 2, 3, 4], [5, 6, 7, 8]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_edge_case_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_edge_case_single_element_list(self):
        input_list = [[3]]
        expected_output = [[3]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_corner_case_already_sorted(self):
        input_list = [[1, 2, 3, 4], [5, 6, 7, 8]]
        expected_output = [[1, 2, 3, 4], [5, 6, 7, 8]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_corner_case_reverse_sorted(self):
        input_list = [[4, 3, 2, 1], [8, 7, 6, 5]]
        expected_output = [[1, 2, 3, 4], [5, 6, 7, 8]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sort_sublists(104_code)

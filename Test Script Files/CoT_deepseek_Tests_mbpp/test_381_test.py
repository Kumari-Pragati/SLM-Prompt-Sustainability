import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):

    def test_typical_case(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 1
        expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_output)

    def test_typical_case_with_duplicates(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 3]]
        index_no = 2
        expected_output = [[1, 2, 3], [7, 8, 3], [4, 5, 6]]
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_output)

    def test_edge_case_with_empty_list(self):
        list_data = []
        index_no = 0
        expected_output = []
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_output)

    def test_edge_case_with_single_element_list(self):
        list_data = [[1, 2, 3]]
        index_no = 1
        expected_output = [[1, 2, 3]]
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_output)

    def test_edge_case_with_negative_index(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = -1
        expected_output = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_output)

    def test_invalid_index(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 3
        with self.assertRaises(IndexError):
            index_on_inner_list(list_data, index_no)

import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):

    def test_typical_case(self):
        list_data = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        index_no = 1
        expected_output = [[2, 3, 1], [5, 6, 4], [8, 9, 7]]
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_output)

    def test_edge_case_with_same_values(self):
        list_data = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        index_no = 0
        expected_output = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_output)

    def test_boundary_case_with_empty_list(self):
        list_data = []
        index_no = 0
        expected_output = []
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_output)

    def test_boundary_case_with_negative_index(self):
        list_data = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        index_no = -1
        expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_output)

    def test_corner_case_with_large_index(self):
        list_data = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        index_no = 10
        expected_output = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_output)

import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):
    def test_typical_use_case(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 1
        expected_result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_result)

    def test_edge_condition(self):
        list_data = []
        index_no = 0
        expected_result = []
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_result)

    def test_boundary_condition(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 3
        expected_result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_result)

    def test_invalid_input(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 'a'
        with self.assertRaises(TypeError):
            index_on_inner_list(list_data, index_no)

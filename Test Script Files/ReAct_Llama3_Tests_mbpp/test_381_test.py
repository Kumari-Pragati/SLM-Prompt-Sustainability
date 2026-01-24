import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):

    def test_typical_case(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 1
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_edge_case(self):
        list_data = [[1, 2, 3], [4, 5, 6]]
        index_no = 1
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [[1, 2, 3], [4, 5, 6]])

    def test_edge_case_empty_list(self):
        list_data = []
        index_no = 1
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [])

    def test_edge_case_single_element_list(self):
        list_data = [[1, 2, 3]]
        index_no = 1
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [[1, 2, 3]])

    def test_edge_case_invalid_index(self):
        list_data = [[1, 2, 3], [4, 5, 6]]
        index_no = 3
        with self.assertRaises(TypeError):
            index_on_inner_list(list_data, index_no)

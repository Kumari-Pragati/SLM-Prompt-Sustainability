import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):

    def test_typical_input(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 1
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_edge_case_index_zero(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 0
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [[x for x in zip(*list_data)]])

    def test_edge_case_index_last(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 2
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_invalid_input_non_integer(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 'a'
        with self.assertRaises(TypeError):
            index_on_inner_list(list_data, index_no)

    def test_invalid_input_out_of_range(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 3
        with self.assertRaises(IndexError):
            index_on_inner_list(list_data, index_no)

import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):

    def test_simple_input(self):
        list_data = [[1, 2], [3, 4], [5, 6]]
        index_no = 0
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [[1, 2], [3, 4], [5, 6]])

    def test_edge_case_empty_list(self):
        list_data = []
        index_no = 0
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [])

    def test_edge_case_index_out_of_range(self):
        list_data = [[1, 2], [3, 4], [5, 6]]
        index_no = 2
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [[5, 6], [1, 2], [3, 4]])

    def test_complex_case_same_values(self):
        list_data = [[1, 2], [1, 2], [1, 2]]
        index_no = 0
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [[1, 2], [1, 2], [1, 2]])

    def test_complex_case_negative_values(self):
        list_data = [[-1, 2], [-3, 4], [-5, 6]]
        index_no = 0
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [[-1, 2], [-3, 4], [-5, 6]])

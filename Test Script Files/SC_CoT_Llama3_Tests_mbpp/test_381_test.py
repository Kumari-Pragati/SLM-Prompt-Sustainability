import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):

    def test_typical_inputs(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 1
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, sorted(list_data, key=itemgetter(1)))

    def test_edge_cases(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 0
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, sorted(list_data, key=itemgetter(0)))

    def test_edge_cases_negative_index(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = -1
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, sorted(list_data, key=itemgetter(2)))

    def test_empty_list(self):
        list_data = []
        index_no = 0
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [])

    def test_list_with_single_element(self):
        list_data = [[1, 2, 3]]
        index_no = 1
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, sorted(list_data, key=itemgetter(1)))

    def test_invalid_input_type(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 'invalid'
        with self.assertRaises(TypeError):
            index_on_inner_list(list_data, index_no)

    def test_invalid_input_value(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 10
        with self.assertRaises(IndexError):
            index_on_inner_list(list_data, index_no)

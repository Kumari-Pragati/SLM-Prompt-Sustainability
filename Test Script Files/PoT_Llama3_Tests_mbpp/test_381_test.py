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

    def test_edge_case2(self):
        list_data = [[1, 2, 3]]
        index_no = 1
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [[1, 2, 3]])

    def test_edge_case3(self):
        list_data = []
        index_no = 1
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [])

    def test_invalid_input(self):
        list_data = [[1, 2, 3]]
        index_no = 'a'
        with self.assertRaises(TypeError):
            index_on_inner_list(list_data, index_no)

    def test_invalid_input2(self):
        list_data = [[1, 2, 3]]
        index_no = 5
        with self.assertRaises(IndexError):
            index_on_inner_list(list_data, index_no)

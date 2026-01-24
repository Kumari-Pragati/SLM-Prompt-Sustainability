import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):
    def test_sorted_list(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 1
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_sorted_list_descending(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 1
        result = index_on_inner_list(list_data, index_no, reverse=True)
        self.assertEqual(result, [[7, 8, 9], [4, 5, 6], [1, 2, 3]])

    def test_empty_list(self):
        list_data = []
        index_no = 1
        result = index_on_inner_list(list_data, index_no)
        self.assertEqual(result, [])

    def test_invalid_index(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 'a'
        with self.assertRaises(TypeError):
            index_on_inner_list(list_data, index_no)

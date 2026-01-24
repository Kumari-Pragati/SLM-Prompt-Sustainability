import unittest
from mbpp_381_code import itemgetter
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):

    def test_index_on_inner_list(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 1
        expected_result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_result)

    def test_index_on_inner_list_with_different_index(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 0
        expected_result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_result)

    def test_index_on_inner_list_with_negative_index(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = -1
        expected_result = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_result)

    def test_index_on_inner_list_with_empty_list(self):
        list_data = []
        index_no = 0
        expected_result = []
        self.assertEqual(index_on_inner_list(list_data, index_no), expected_result)

    def test_index_on_inner_list_with_nonexistent_index(self):
        list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index_no = 3
        self.assertRaises(IndexError, index_on_inner_list, list_data, index_no)

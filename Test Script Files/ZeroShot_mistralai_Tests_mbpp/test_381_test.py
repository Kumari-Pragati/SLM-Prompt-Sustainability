import unittest
from mbpp_381_code import itemgetter
from 381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(index_on_inner_list([], 0), [])

    def test_single_element_list(self):
        self.assertListEqual(index_on_inner_list([[1]], 0), [[1]])

    def test_list_with_single_inner_list(self):
        self.assertListEqual(index_on_inner_list([[1], [2], [3]], 0), [[1], [2], [3]])

    def test_list_with_multiple_inner_lists(self):
        self.assertListEqual(index_on_inner_list([[1, 2], [3, 4], [5, 6]], 1), [[2, 4], [3, 6]])

    def test_list_with_mixed_types(self):
        self.assertListEqual(index_on_inner_list([[1, 'a'], [2, 'b'], [3, 'c']], 1), ['a', 'b', 'c'])

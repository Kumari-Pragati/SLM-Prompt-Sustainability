import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):
    def test_sort_empty_list(self):
        self.assertEqual(index_on_inner_list([], 0), [])

    def test_sort_single_element_list(self):
        self.assertEqual(index_on_inner_list([1], 0), [1])

    def test_sort_list_with_duplicates(self):
        self.assertEqual(index_on_inner_list([1, 2, 1, 3, 2], 1), [2, 2])

    def test_sort_list_with_negative_index(self):
        self.assertRaises(IndexError, lambda: index_on_inner_list([1, 2, 3], -1))

    def test_sort_list_with_invalid_index(self):
        self.assertRaises(IndexError, lambda: index_on_inner_list([1, 2, 3], 4))

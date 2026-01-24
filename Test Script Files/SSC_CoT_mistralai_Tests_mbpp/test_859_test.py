import unittest
from mbpp_859_code import chain, combinations
from copy import deepcopy

from 859_code import sub_lists

class TestSubLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(sub_lists([]), [])

    def test_single_element_list(self):
        self.assertListEqual(sub_lists([1]), [[1]])

    def test_two_elements_list(self):
        self.assertListEqual(sub_lists([1, 2]), [[1], [2], [1, 2]])

    def test_longer_list(self):
        self.assertListEqual(sub_lists([1, 2, 3, 4]), [[1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]])

    def test_negative_index(self):
        self.assertListEqual(sub_lists([1, 2, 3]), [])

    def test_large_index(self):
        self.assertListEqual(sub_lists([1, 2, 3]), [])

    def test_duplicate_elements(self):
        self.assertListEqual(sub_lists([1, 1, 2]), [[1], [1], [2], [1, 1], [1, 2], [1, 1, 2]])

    def test_list_with_empty_sublist(self):
        self.assertListEqual(sub_lists([[], 1, 2]), [[], [1], [2]])

    def test_list_with_nested_sublist(self):
        nested_list = [[1], [2, 3], [4, 5]]
        expected = [[1], [2], [3], [4], [5], [1, 2], [1, 3], [2, 3], [1, 4], [1, 5], [2, 4], [2, 5], [3, 4], [3, 5], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [2, 3, 4], [2, 3, 5]]
        self.assertListEqual(sub_lists(nested_list), expected)

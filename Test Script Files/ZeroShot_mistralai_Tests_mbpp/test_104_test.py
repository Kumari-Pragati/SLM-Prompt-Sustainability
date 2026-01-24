import unittest
from mbpp_104_code import List

from 104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertListEqual(sort_sublists([[1, 2]]), [[[1, 2]]])

    def test_multiple_element_lists(self):
        self.assertListEqual(sort_sublists([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]),
                             [[[[1, 2]], [[3, 4]]], [[[5, 6]], [[7, 8]]], [[[9, 10]], [[11, 12]]]])

    def test_mixed_sublists(self):
        self.assertListEqual(sort_sublists([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]], [[0, 0], [0, 0]]]),
                             [[[[1, 2]], [[3, 4]]], [[[5, 6]], [[7, 8]]], [[[9, 10]], [[11, 12]]], [[[0, 0]], [[0, 0]]]])

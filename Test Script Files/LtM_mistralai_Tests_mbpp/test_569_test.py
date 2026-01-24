import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_simple_list(self):
        self.assertListEqual(sort_sublists([[1, 2], [3, 4], [5, 6]]), [[[1, 2], [1, 2]], [[3, 4], 3, 4], [[5, 6], 5, 6]])

    def test_empty_list(self):
        self.assertListEqual(sort_sublists([]), [])

    def test_single_sublist(self):
        self.assertListEqual(sort_sublists([[1]]), [[1]])

    def test_negative_numbers(self):
        self.assertListEqual(sort_sublists([[-1, -2], [3, 4], [-5, -6]]), [[[-1, -2], -1, -2], [[3, 4], 3, 4], [[-5, -6], -5, -6]])

    def test_mixed_types(self):
        self.assertRaises(TypeError, sort_sublists, [[1, 'a'], [2, 'b'], [3, 'c']])

    def test_nested_lists(self):
        self.assertListEqual(sort_sublists([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]), [[[[1, 2], [1, 2]], [[3, 4], 3, 4]], [[[5, 6], 5, 6], [7, 8]], [[[9, 10], 9, 10], [11, 12]]])

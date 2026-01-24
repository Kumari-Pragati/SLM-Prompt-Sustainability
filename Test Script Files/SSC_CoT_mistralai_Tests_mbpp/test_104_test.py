import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_sort_sublists_normal(self):
        self.assertListEqual(sort_sublists([[1, 2], [3, 4], [5, 6]]), [[[1, 2], [1, 2]], [[3, 4], [3, 4]], [[5, 6], [5, 6]]])
        self.assertListEqual(sort_sublists([['a', 'b'], ['c', 'd'], ['e', 'f']]), [[['a', 'b'], ['a', 'b']], ['c', 'd'], ['e', 'f']])

    def test_sort_sublists_edge_cases(self):
        self.assertListEqual(sort_sublists([[0, 0], [1, 1], [2, 2]]), [[[0, 0], [0, 0]], [[1, 1], [1, 1]], [[2, 2], [2, 2]]])
        self.assertListEqual(sort_sublists([[9, 9], [8, 8], [7, 7]]), [[[9, 9], [9, 9]], [[8, 8], [8, 8]], [[7, 7], [7, 7]]])
        self.assertListEqual(sort_sublists([[10, 10], [9, 9], [8, 8]]), [[[9, 9], [9, 9]], [[8, 8], [8, 8]], [[10, 10], [10, 10]]])
        self.assertListEqual(sort_sublists([[-1, -1], [-2, -2], [-3, -3]]), [[[-3, -3], [-3, -3]], [[-2, -2], [-2, -2]], [[-1, -1], [-1, -1]]])

    def test_sort_sublists_empty_lists(self):
        self.assertListEqual(sort_sublists([]), [])
        self.assertListEqual(sort_sublists([[]]), [[[]]])
        self.assertListEqual(sort_sublists([[1], []]), [[[1]]])
        self.assertListEqual(sort_sublists([[], [1]]), [[[]], [[1]]])
        self.assertListEqual(sort_sublists([[1], [2], []]), [[[1]], [[2]]])
        self.assertListEqual(sort_sublists([[], [1], [2]]), [[[]], [[1]], [[2]]])

    def test_sort_sublists_mixed_types(self):
        self.assertRaises(TypeError, sort_sublists, [[1, 'a'], [2, 'b'], [3, 'c']])
        self.assertRaises(TypeError, sort_sublists, [[1, 2.5], [3, 4], [5, 'e']])
        self.assertRaises(TypeError, sort_sublists, [[1, 2], [3, 'b'], [5, 6]])

import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_sublists([[1, 2]]), [[[1, 2]]])

    def test_multiple_sublists(self):
        self.assertEqual(sort_sublists([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]),
                         [[[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[[9, 10], [11, 12]]]],
                          [[[3, 4], [1, 2]], [[7, 8], [5, 6]], [[[11, 12], [9, 10]]]],
                          [[[5, 6], [7, 8]], [[3, 4], [1, 2]], [[[11, 12], [9, 10]]]],
                          [[[7, 8], [5, 6]], [[1, 2], [3, 4]], [[[11, 12], [9, 10]]]],
                          [[[5, 6], [7, 8]], [[3, 4], [1, 2]], [[[9, 10], [11, 12]]]],
                          [[[7, 8], [5, 6]], [[1, 2], [3, 4]], [[[11, 12], [9, 10]]]],
                          [[[5, 6], [7, 8]], [[3, 4], [1, 2]], [[[9, 10], [11, 12]]]],
                          [[[7, 8], [5, 6]], [[1, 2], [3, 4]], [[[11, 12], [9, 10]]]],
                          [[[5, 6], [7, 8]], [[3, 4], [1, 2]], [[[9, 10], [11, 12]]]],
                          [[[7, 8], [5, 6]], [[1, 2], [3, 4]], [[[11, 12], [9, 10]]]])

    def test_mixed_types(self):
        self.assertRaises(TypeError, sort_sublists, [[1, 2], 'abc', [3, 4]])

    def test_invalid_sublist(self):
        self.assertRaises(TypeError, sort_sublists, [[1, 2, 3]])

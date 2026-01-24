import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(sort_sublists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_empty_input(self):
        self.assertListEqual(sort_sublists([]), [])

    def test_single_input(self):
        self.assertListEqual(sort_sublists([[1]]), [[1]])

    def test_single_element_sublist(self):
        self.assertListEqual(sort_sublists([[1]]), [[1]])
        self.assertListEqual(sort_sublists([[1, ], [2, ], [3, ]]), [[1], [2], [3]])

    def test_mixed_types(self):
        self.assertRaises(TypeError, sort_sublists, [[1, 'a'], [2, 'b'], [3, 'c']])

    def test_negative_numbers(self):
        self.assertListEqual(sort_sublists([[-1, -2, -3], [4, 5, 6], [-7, -8, -9]]), [[-1, -2, -3], [4, 5, 6], [-7, -8, -9]])

    def test_duplicate_elements(self):
        self.assertListEqual(sort_sublists([[1, 1, 2], [4, 4, 5], [7, 7, 8]]), [[1, 1, 2], [4, 4, 5], [7, 7, 8]])

    def test_reverse_order(self):
        self.assertListEqual(sort_sublists([[3, 2, 1], [6, 5, 4], [9, 8, 7]]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

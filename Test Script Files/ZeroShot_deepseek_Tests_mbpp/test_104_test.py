import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_sublist(self):
        self.assertEqual(sort_sublists([[2, 1]]), [[1, 2]])

    def test_multiple_sublists(self):
        self.assertEqual(sort_sublists([[3, 2, 1], [4, 5, 6]]), [[1, 2, 3], [4, 5, 6]])

    def test_unsorted_sublists(self):
        self.assertEqual(sort_sublists([[1, 3, 2], [4, 5, 6]]), [[1, 2, 3], [4, 5, 6]])

    def test_duplicate_values(self):
        self.assertEqual(sort_sublists([[3, 2, 2], [4, 5, 6]]), [[2, 2, 3], [4, 5, 6]])

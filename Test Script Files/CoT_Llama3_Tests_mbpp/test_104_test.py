import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_sublists([[1, 2, 3]]), [[1, 2, 3]])

    def test_multiple_sublists(self):
        self.assertEqual(sort_sublists([[3, 2, 1], [4, 5, 6], [1, 2, 3]]), [[1, 2, 3], [3, 2, 1], [4, 5, 6]])

    def test_sublists_with_duplicates(self):
        self.assertEqual(sort_sublists([[3, 2, 1], [4, 5, 5], [1, 2, 3]]), [[1, 2, 3], [3, 2, 1], [4, 5, 5]])

    def test_sublists_with_empty_sublist(self):
        self.assertEqual(sort_sublists([[3, 2, 1], [], [1, 2, 3]]), [[1, 2, 3], [], [3, 2, 1]])

    def test_sublists_with_empty_sublist_and_duplicates(self):
        self.assertEqual(sort_sublists([[3, 2, 1], [], [1, 2, 3, 4, 5, 5]]), [[1, 2, 3, 4, 5, 5], [], [3, 2, 1]])

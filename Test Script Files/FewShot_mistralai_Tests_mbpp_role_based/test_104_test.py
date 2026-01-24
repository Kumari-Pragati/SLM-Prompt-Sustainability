import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_sorted_sublists(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4], [5, 6]]), [[[1, 2], [1, 2]], [[3, 4], [3, 4]], [[5, 6], [5, 6]]])

    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_sublist(self):
        self.assertEqual(sort_sublists([[1]]), [[[1]]])

    def test_sublist_with_duplicates(self):
        self.assertEqual(sort_sublists([[1, 1], [2, 2]]), [[[1, 1]], [[2, 2]]])

    def test_sublist_with_mixed_elements(self):
        self.assertEqual(sort_sublists([[2, 'a'], [1, 'b'], [3, 'a']]), [[[1, 'b'], [1, 'b']], [[2, 'a'], [2, 'a']], [[3, 'a'], [3, 'a']]])

import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_sorted_list(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4], [5, 6]]), [[[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]])

    def test_sorted_by_length(self):
        self.assertEqual(sort_sublists([[3, 2], [1, 4], [5, 6]]), [[[1, 4], [3, 2], [5, 6]], [[1, 4], [3, 2], [5, 6]]])

    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_sublists([[1]]), [[[1]]])

    def test_list_with_single_sublist(self):
        self.assertEqual(sort_sublists([[1, 2]]), [[[1, 2]]])

    def test_list_with_mixed_sublists(self):
        self.assertEqual(sort_sublists([[3, 2], [1, 4], [5, 6], [7, 8]]), [[[1, 4], [3, 2], [5, 6], [7, 8]], [[1, 4], [3, 2], [5, 6], [7, 8]]])

import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_sort_simple_list(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4], [5, 6]]), [[[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]])

    def test_sort_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_sort_single_element_list(self):
        self.assertEqual(sort_sublists([[1]]), [[[1]]])

    def test_sort_list_with_single_sublist(self):
        self.assertEqual(sort_sublists([[1, 2]]), [[[1, 2]]])

    def test_sort_list_with_mixed_sublists(self):
        self.assertEqual(sort_sublists([[1, 2], [3], [4, 5, 6]]), [[[1, 2], [3], [4, 5, 6]], [[1, 2], [3], [4, 5, 6]]])

    def test_sort_list_with_longer_sublists_first(self):
        self.assertEqual(sort_sublists([[5, 2], [1, 3]]), [[[5, 2], [1, 3]], [[5, 2], [1, 3]]])

    def test_sort_list_with_longer_sublists_last(self):
        self.assertEqual(sort_sublists([[1, 3], [5, 2]]), [[[1, 3], [5, 2]], [[1, 3], [5, 2]]])

    def test_sort_list_with_equal_length_sublists(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4]]), [[[1, 2], [3, 4]], [[1, 2], [3, 4]]])

    def test_sort_list_with_empty_sublists(self):
        self.assertEqual(sort_sublists([[], [1, 2], [3, 4]]), [[[], [1, 2], [3, 4]], [[], [1, 2], [3, 4]]])

import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):
    def test_normal(self):
        self.assertListEqual(merge_sorted_list([1, 3, 5], [2, 4, 6], []), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(merge_sorted_list([1, 3, 5], [2, 4], [6]), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(merge_sorted_list([], [2, 4, 6], [1, 3, 5]), [1, 2, 3, 4, 5, 6])

    def test_edge_cases(self):
        self.assertListEqual(merge_sorted_list([], [], []), [])
        self.assertListEqual(merge_sorted_list([], [1], []), [1])
        self.assertListEqual(merge_sorted_list([1], [], []), [1])
        self.assertListEqual(merge_sorted_list([], [1], [1]), [1])

    def test_empty_lists(self):
        self.assertListEqual(merge_sorted_list([], []), [])
        self.assertListEqual(merge_sorted_list([], [1]), [1])
        self.assertListEqual(merge_sorted_list([1], []), [1])

    def test_single_list(self):
        self.assertListEqual(merge_sorted_list([1]), [1])
        self.assertListEqual(merge_sorted_list([1, 2]), [1, 2])
        self.assertListEqual(merge_sorted_list([2, 1]), [1, 2])

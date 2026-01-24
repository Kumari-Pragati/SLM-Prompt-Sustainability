import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(merge_sorted_list([1, 2, 3], [4, 5, 6], []), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(merge_sorted_list([1, 2, 3], [], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(merge_sorted_list([], [4, 5, 6], [1, 2, 3]), [1, 2, 3, 4, 5, 6])

    def test_edge_cases(self):
        self.assertListEqual(merge_sorted_list([], [], []), [])
        self.assertListEqual(merge_sorted_list([], [1], []), [1])
        self.assertListEqual(merge_sorted_list([1], [], []), [1])
        self.assertListEqual(merge_sorted_list([], [1], [1]), [1])

    def test_complex(self):
        self.assertListEqual(merge_sorted_list([3, 5, 7], [2, 4, 6], [1, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertListEqual(merge_sorted_list([1, 3, 5], [2, 4, 6], [7, 8, 9]), [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertListEqual(merge_sorted_list([1, 3, 5], [2, 4], [7, 8, 9]), [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertListEqual(merge_sorted_list([1, 3, 5], [], [7, 8, 9]), [1, 3, 5, 7, 8, 9])
        self.assertListEqual(merge_sorted_list([], [2, 4], [1, 3, 5]), [1, 2, 3, 4])
        self.assertListEqual(merge_sorted_list([], [2, 4], [1, 3]), [1, 2, 3, 4])
        self.assertListEqual(merge_sorted_list([], [2], [1, 3]), [1, 2, 3])

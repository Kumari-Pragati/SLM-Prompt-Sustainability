import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(merge_sorted_list([1, 3, 5], [2, 4, 6], [7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_single_list(self):
        self.assertListEqual(merge_sorted_list([1, 3, 5], []), [1, 3, 5])
        self.assertListEqual(merge_sorted_list([], [2, 4, 6]), [2, 4, 6])

    def test_empty_list(self):
        self.assertListEqual(merge_sorted_list([], [], []), [])

    def test_duplicates(self):
        self.assertListEqual(merge_sorted_list([1, 1, 3, 5], [2, 2, 4, 6], [7, 7, 8, 8]), [1, 1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 8])

    def test_reverse_order(self):
        self.assertListEqual(merge_sorted_list([5, 3, 1], [6, 4, 2], [9, 8, 7]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

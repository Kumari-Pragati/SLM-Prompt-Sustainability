import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(merge_sorted_list([], [], []), [])

    def test_single_element_lists(self):
        self.assertEqual(merge_sorted_list([1], [2], [3]), [1, 2, 3])

    def test_sorted_lists(self):
        self.assertEqual(merge_sorted_list([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_unsorted_lists(self):
        self.assertEqual(merge_sorted_list([3, 1, 2], [4, 5, 6], [7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_lists_with_duplicates(self):
        self.assertEqual(merge_sorted_list([1, 2, 2, 3], [4, 4, 5, 6], [7, 8, 9]), [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9])

    def test_lists_with_negative_numbers(self):
        self.assertEqual(merge_sorted_list([-1, 0, 1], [-2, -1, 0], [0, 1, 2]), [-2, -1, -1, 0, 0, 1, 1, 2])

    def test_lists_with_zero(self):
        self.assertEqual(merge_sorted_list([0, 1, 2], [0, 1, 2], [0, 1, 2]), [0, 0, 0, 1, 1, 1, 2, 2, 2])

import unittest
from mbpp_152_code import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(merge_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_duplicates_list(self):
        self.assertEqual(merge_sort([2, 1, 3, 3, 2, 1]), [1, 1, 2, 2, 3, 3])

    def test_list_with_duplicates_and_empty(self):
        self.assertEqual(merge_sort([2, 1, 3, 3, 2, 1, 0, 0]), [0, 0, 1, 1, 2, 2, 3, 3])

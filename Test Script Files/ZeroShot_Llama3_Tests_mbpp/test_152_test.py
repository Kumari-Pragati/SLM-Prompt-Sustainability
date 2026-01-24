import unittest
from mbpp_152_code import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(merge_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(merge_sort([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])

    def test_duplicates(self):
        self.assertEqual(merge_sort([5, 2, 8, 2, 1, 9]), [1, 2, 2, 5, 8, 9])

    def test_reverse_sorted_list(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_large_list(self):
        self.assertEqual(merge_sort([5, 2, 8, 1, 9, 3, 4, 6, 7, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

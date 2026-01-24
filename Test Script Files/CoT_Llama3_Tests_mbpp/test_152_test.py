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
        self.assertEqual(merge_sort([5, 2, 8, 1, 3]), [1, 2, 3, 5, 8])

    def test_duplicates(self):
        self.assertEqual(merge_sort([5, 2, 8, 1, 3, 5]), [1, 2, 3, 5, 5, 8])

    def test_reverse_sorted_list(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates_and_reverse_sorted(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1, 5, 5]), [1, 2, 3, 4, 5, 5, 5])

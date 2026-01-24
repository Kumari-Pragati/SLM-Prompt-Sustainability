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
        self.assertEqual(merge_sort([5, 2, 8, 3, 1, 4]), [1, 2, 3, 4, 5, 8])

    def test_list_with_duplicates(self):
        self.assertEqual(merge_sort([5, 2, 8, 3, 3, 1, 4, 4]), [1, 2, 3, 3, 4, 4, 5, 8])

    def test_list_with_negative_numbers(self):
        self.assertEqual(merge_sort([-5, -2, -8, -3, -1, -4]), [-8, -5, -4, -3, -2, -1])

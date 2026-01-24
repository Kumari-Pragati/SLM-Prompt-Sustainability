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

    def test_list_with_duplicates(self):
        self.assertEqual(merge_sort([5, 2, 8, 5, 1, 3]), [1, 2, 3, 5, 5, 8])

    def test_list_with_negative_numbers(self):
        self.assertEqual(merge_sort([-5, 2, -8, 1, 3]), [-8, -5, 1, 2, 3])

    def test_list_with_zero(self):
        self.assertEqual(merge_sort([0, 2, 8, 1, 3]), [0, 1, 2, 3, 8])

    def test_list_with_zero_and_negative_numbers(self):
        self.assertEqual(merge_sort([-5, 0, -8, 1, 3]), [-8, -5, 0, 1, 3])

    def test_list_with_zero_and_positive_numbers(self):
        self.assertEqual(merge_sort([0, 2, 8, 1, 3]), [0, 1, 2, 3, 8])

    def test_list_with_zero_and_duplicates(self):
        self.assertEqual(merge_sort([0, 0, 2, 8, 1, 3]), [0, 0, 1, 2, 3, 8])

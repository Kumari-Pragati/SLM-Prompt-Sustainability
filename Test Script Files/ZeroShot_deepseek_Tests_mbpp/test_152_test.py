import unittest
from mbpp_152_code import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(merge_sort([1, 2, 2, 1]), [1, 1, 2, 2])

    def test_negative_numbers(self):
        self.assertEqual(merge_sort([-5, -4, -3, -2, -1]), [-5, -4, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(merge_sort([-5, 4, 0, -3, 2]), [-5, -3, 0, 2, 4])

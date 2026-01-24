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
        self.assertEqual(merge_sort([5, 2, 8, 3, 1]), [1, 2, 3, 5, 8])

    def test_list_with_duplicates(self):
        self.assertEqual(merge_sort([5, 2, 8, 3, 1, 5]), [1, 2, 3, 5, 5, 8])

    def test_edge_case_list(self):
        self.assertEqual(merge_sort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

    def test_max_value_list(self):
        self.assertEqual(merge_sort([100, 50, 20, 10, 5]), [5, 10, 20, 50, 100])

    def test_min_value_list(self):
        self.assertEqual(merge_sort([-100, -50, -20, -10, -5]), [-100, -50, -20, -10, -5])

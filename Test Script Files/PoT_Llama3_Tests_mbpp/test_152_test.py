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

    def test_duplicates(self):
        self.assertEqual(merge_sort([3, 3, 1, 1, 4, 5, 5, 2, 2, 6]), [1, 1, 2, 2, 3, 3, 4, 5, 5, 6])

    def test_edge_case(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_edge_case2(self):
        self.assertEqual(merge_sort([1, 2]), [1, 2])

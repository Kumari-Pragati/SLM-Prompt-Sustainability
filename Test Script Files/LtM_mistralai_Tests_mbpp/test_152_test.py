import unittest
from mbpp_152_code import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_simple_list(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_reverse_list(self):
        self.assertEqual(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_duplicates(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_large_list(self):
        self.assertEqual(merge_sort([1000000, 999999, 999998, 999997, 999996]), [999996, 999997, 999998, 999999, 1000000])

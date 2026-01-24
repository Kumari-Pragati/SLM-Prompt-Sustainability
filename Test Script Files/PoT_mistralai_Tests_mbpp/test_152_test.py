import unittest
from mbpp_152_code import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_simple_list(self):
        self.assertEqual(merge_sort([3, 5, 1, 2, 8, 7, 6]), [1, 2, 3, 5, 6, 7, 8])

    def test_reverse_list(self):
        self.assertEqual(merge_sort([8, 7, 6, 5, 3, 2, 1]), [1, 2, 3, 5, 6, 7, 8])

    def test_duplicates(self):
        self.assertEqual(merge_sort([3, 3, 1, 2, 8, 7, 6, 3]), [1, 2, 3, 3, 6, 7, 8])

    def test_long_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_long_list_reverse_order(self):
        self.assertEqual(merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_list_with_zero(self):
        self.assertEqual(merge_sort([-1, 0, 1]), [-1, 0, 1])

    def test_list_with_negative_numbers(self):
        self.assertEqual(merge_sort([-5, -3, -1, 1, 3, 5]), [-5, -3, -1, 1, 3, 5])

    def test_list_with_large_numbers(self):
        self.assertEqual(merge_sort([1000000, 999999, 999998, 1, 2, 3]), [1, 2, 3, 999998, 999999, 1000000])

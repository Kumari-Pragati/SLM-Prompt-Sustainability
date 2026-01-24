import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_radix_sort_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_radix_sort_single_element(self):
        self.assertEqual(radix_sort([5]), [5])

    def test_radix_sort_sorted_list(self):
        self.assertEqual(radix_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_radix_sort_unsorted_list(self):
        self.assertEqual(radix_sort([5, 2, 8, 6, 1, 9]), [1, 2, 5, 6, 8, 9])

    def test_radix_sort_negative_numbers(self):
        self.assertEqual(radix_sort([-5, -2, -8, -6, -1, -9]), [-9, -8, -6, -5, -2, -1])

    def test_radix_sort_duplicates(self):
        self.assertEqual(radix_sort([5, 2, 8, 6, 1, 9, 5, 2, 8, 6, 1, 9]), [1, 2, 2, 5, 5, 6, 6, 8, 8, 9, 9])

    def test_radix_sort_large_list(self):
        self.assertEqual(radix_sort([5, 2, 8, 6, 1, 9, 7, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2, 8, 9, 1, 3, 4, 0, 6, 5, 2
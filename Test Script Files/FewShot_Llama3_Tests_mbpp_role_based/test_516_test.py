import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(radix_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(radix_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(radix_sort([5, 2, 8, 6, 1, 9, 3, 4, 7]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_negative_numbers(self):
        self.assertEqual(radix_sort([-5, -2, -8, -6, -1, -9, -3, -4, -7]), [-9, -8, -7, -6, -5, -4, -3, -2, -1])

    def test_large_numbers(self):
        self.assertEqual(radix_sort([123, 456, 789, 101, 202, 303, 404, 505, 606]), [101, 202, 303, 404, 505, 606, 123, 456, 789])

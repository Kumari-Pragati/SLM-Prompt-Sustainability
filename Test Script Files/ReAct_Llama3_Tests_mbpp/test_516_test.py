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
        self.assertEqual(radix_sort([5, 2, 8, 3, 1, 6, 4]), [1, 2, 3, 4, 5, 6, 8])

    def test_negative_numbers(self):
        self.assertEqual(radix_sort([-5, -2, -8, -3, -1, -6, -4]), [-8, -6, -5, -4, -3, -2, -1])

    def test_duplicates(self):
        self.assertEqual(radix_sort([5, 2, 8, 3, 1, 6, 4, 5]), [1, 2, 3, 4, 5, 5, 6, 8])

    def test_large_numbers(self):
        self.assertEqual(radix_sort([123456, 654321, 111111, 222222, 333333, 444444, 555555]), [111111, 222222, 333333, 444444, 555555, 654321, 123456])

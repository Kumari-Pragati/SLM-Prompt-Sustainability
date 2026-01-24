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
        self.assertEqual(radix_sort([5, 2, 8, 6, 1, 9, 3, 7, 4]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_radix_sort_duplicates(self):
        self.assertEqual(radix_sort([5, 2, 8, 6, 1, 9, 3, 7, 4, 4]), [1, 2, 3, 4, 4, 5, 6, 7, 8, 9])

    def test_radix_sort_negative_numbers(self):
        self.assertEqual(radix_sort([-5, -2, -8, -6, -1, -9, -3, -7, -4]), [-9, -8, -7, -6, -5, -4, -3, -2, -1])

    def test_radix_sort_mixed_type(self):
        with self.assertRaises(TypeError):
            radix_sort([5, 2, 'a', 8, 6, 1, 9, 3, 7, 4])

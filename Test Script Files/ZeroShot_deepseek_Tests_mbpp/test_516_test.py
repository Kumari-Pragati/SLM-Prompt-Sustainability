import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_radix_sort_ascending(self):
        self.assertEqual(radix_sort([3, 2, 9, 4, 5, 1]), [1, 2, 3, 4, 5, 9])

    def test_radix_sort_descending(self):
        self.assertEqual(radix_sort([9, 8, 7, 6, 5, 4]), [4, 5, 6, 7, 8, 9])

    def test_radix_sort_single_element(self):
        self.assertEqual(radix_sort([5]), [5])

    def test_radix_sort_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_radix_sort_negative_numbers(self):
        self.assertEqual(radix_sort([-1, -9, -4, -6]), [-9, -6, -4, -1])

    def test_radix_sort_mixed_numbers(self):
        self.assertEqual(radix_sort([3, -1, 2, -5, 1]), [-5, -1, 1, 2, 3])

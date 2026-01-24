import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(radix_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_single_element(self):
        self.assertEqual(radix_sort([5]), [5])

    def test_already_sorted(self):
        self.assertEqual(radix_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(radix_sort([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]), [-9, -6, -5, -5, -5, -4, -3, -3, -2, -1, -1])

    def test_mixed_positive_negative(self):
        self.assertEqual(radix_sort([3, -1, 4, -1, 5, -9, 2, 6, -5, 3, -5]), [-9, -5, -1, -1, 2, 3, 3, 4, 5, 5, 6])

    def test_large_numbers(self):
        self.assertEqual(radix_sort([100, 200, 300, 400, 500]), [100, 200, 300, 400, 500])

    def test_duplicate_numbers(self):
        self.assertEqual(radix_sort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

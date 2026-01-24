import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):
    def test_sorts_positive_numbers(self):
        self.assertEqual(radix_sort([34, 2, 12, 1, 5, 78, 9, 45]), [1, 2, 34, 9, 12, 45, 5, 78])

    def test_sorts_negative_numbers(self):
        self.assertEqual(radix_sort([-34, -2, -12, -1, -5, -78, -9, -45]), [-45, -34, -9, -12, -1, -78, -5, -2])

    def test_sorts_zero(self):
        self.assertEqual(radix_sort([0]), [0])

    def test_sorts_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_sorts_mixed_numbers(self):
        self.assertEqual(radix_sort([34, -2, 12, 0, 5, -78, 9, 45, -1]), [0, -1, -2, 34, 5, -78, 9, 45, 12])

    def test_sorts_large_numbers(self):
        self.assertEqual(radix_sort([123456789, 987654321, 123, 456]), [123, 456, 123456789, 987654321])

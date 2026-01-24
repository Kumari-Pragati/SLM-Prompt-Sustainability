import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_single_element(self):
        self.assertEqual(radix_sort([1]), [1])

    def test_simple_list(self):
        self.assertEqual(radix_sort([384917, 293618, 192837, 82127, 293618, 384917]), [82127, 192837, 293618, 293618, 384917, 384917])

    def test_reverse_list(self):
        self.assertEqual(radix_sort([3419, 147, 5236, 8753, 6587, 3419]), [147, 3419, 3419, 5236, 6587, 8753])

    def test_large_numbers(self):
        self.assertEqual(radix_sort([123456789, 987654321, 456789123]), [123456789, 456789123, 987654321])

    def test_negative_numbers(self):
        self.assertEqual(radix_sort([-123, -456, -789]), [-789, -456, -123])

    def test_mixed_numbers(self):
        self.assertEqual(radix_sort([-123, 456, -789, 12345, -678, 98765]), [-678, -789, -123, 456, 12345, 98765])

    def test_large_mixed_numbers(self):
        self.assertEqual(radix_sort([-123456789, 987654321, 456789123, -123, 0]), [-123456789, -123, 0, 456789123, 987654321])

import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(radix_sort([38, 27, 43, 19, 2, 46, 55]), [2, 19, 38, 27, 43, 46, 55])
        self.assertEqual(radix_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_edge_cases(self):
        self.assertEqual(radix_sort([]), [])
        self.assertEqual(radix_sort([1000000000]), [1000000000])
        self.assertEqual(radix_sort([1, 10, 100, 1000, 10000, 100000, 1000000]), [1, 10, 100, 1000, 10000, 100000, 1000000])

    def test_complex(self):
        self.assertEqual(radix_sort([1000000, 1, 100000, 1000, 10, 9, 8, 7, 6, 5, 4, 3, 2]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000, 100000, 1000000])
        self.assertEqual(radix_sort([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]), [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])

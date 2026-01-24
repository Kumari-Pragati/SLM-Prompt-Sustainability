import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(radix_sort([38, 20, 4, 2, 5, 1]), [1, 2, 4, 5, 20, 38])
        self.assertEqual(radix_sort([10, -20, 3, 50, 60, 80]), [-20, 3, 10, 50, 60, 80])
        self.assertEqual(radix_sort([10000, 1000, 100, 10, 1]), [1, 10, 100, 1000, 10000])

    def test_edge_case_single_digit(self):
        self.assertEqual(radix_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_zero(self):
        self.assertEqual(radix_sort([0]), [0])
        self.assertEqual(radix_sort([0, 0, 0]), [0, 0, 0])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(radix_sort([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])

    def test_edge_case_large_numbers(self):
        self.assertEqual(radix_sort([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]),
                         [1000000001, 1000000002, 1000000003, 1000000004, 1000000005])

    def test_corner_case_empty_list(self):
        self.assertEqual(radix_sort([]), [])

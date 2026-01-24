import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_single_element(self):
        self.assertEqual(radix_sort([1]), [1])

    def test_simple_list(self):
        self.assertEqual(radix_sort([37, 15, 92, 5, 74, 25]), [5, 15, 25, 37, 50, 74])

    def test_reverse_list(self):
        self.assertEqual(radix_sort([100, 99, 98, 97, 96]), [96, 97, 98, 99, 100])

    def test_zero_list(self):
        self.assertEqual(radix_sort([0]), [0])

    def test_negative_numbers(self):
        self.assertEqual(radix_sort([-3, -2, -1, 0, 1, 2, 3]), [-3, -2, -1, 0, 1, 2, 3])

    def test_large_numbers(self):
        self.assertEqual(radix_sort([123456789, 987654321, 123000000]), [123000000, 987654321, 123456789])

    def test_max_radix(self):
        self.assertEqual(radix_sort([10**10, 10**9, 10**8]), [10**8, 10**9, 10**10])

    def test_max_radix_overflow(self):
        with self.assertRaises(ValueError):
            radix_sort([10**18, 10**17, 10**16])

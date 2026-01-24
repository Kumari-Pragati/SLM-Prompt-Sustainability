import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_single_element(self):
        self.assertEqual(radix_sort([1]), [1])

    def test_simple_list(self):
        self.assertEqual(radix_sort([3, 4, 1, 5, 2]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(radix_sort([-3, -2, -1, 0, 1, 2, 3]), [-3, -2, -1, 0, 1, 2, 3])

    def test_large_numbers(self):
        self.assertEqual(radix_sort([123456789, 987654321, 123, 456, 7890]), [123, 456, 123456789, 7890, 987654321])

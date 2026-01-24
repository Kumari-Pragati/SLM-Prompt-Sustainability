import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]), [2, 24, 45, 66, 75, 90, 170, 802])

    def test_single_element(self):
        self.assertEqual(radix_sort([5]), [5])

    def test_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_negative_numbers(self):
        self.assertEqual(radix_sort([-1, -5, -10]), [-10, -5, -1])

    def test_large_numbers(self):
        self.assertEqual(radix_sort([10000, 20000, 30000]), [10000, 20000, 30000])

    def test_duplicate_elements(self):
        self.assertEqual(radix_sort([10, 10, 10]), [10, 10, 10])

    def test_large_numbers_with_duplicates(self):
        self.assertEqual(radix_sort([10000, 20000, 10000]), [10000, 10000, 20000])

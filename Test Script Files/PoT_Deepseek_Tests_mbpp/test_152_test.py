import unittest
from mbpp_152_code import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]), [1, 1, 2, 3, 3, 4, 5, 5, 6, 9])

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(merge_sort([5]), [5])

    def test_already_sorted(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(merge_sort([1, 1, 2, 2, 3, 3]), [1, 1, 2, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(merge_sort([-5, -2, -1, 0, 3]), [-5, -2, -1, 0, 3])

    def test_large_numbers(self):
        self.assertEqual(merge_sort([1000, 2000, 3000, 4000]), [1000, 2000, 3000, 4000])

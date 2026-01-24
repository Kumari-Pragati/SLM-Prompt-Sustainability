import unittest
from mbpp_152_code import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_list(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]), [1, 1, 2, 3, 3, 4, 5, 5, 6, 9])

    def test_duplicate_elements(self):
        self.assertEqual(merge_sort([1, 2, 2, 3, 4, 4, 5]), [1, 2, 2, 3, 4, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(merge_sort([-5, -2, -1, 0, 3, 1]), [-5, -2, -1, 0, 1, 3])

    def test_large_numbers(self):
        self.assertEqual(merge_sort([1000, 2000, 3000, 4000, 5000]), [1000, 2000, 3000, 4000, 5000])

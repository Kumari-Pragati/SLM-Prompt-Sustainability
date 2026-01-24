import unittest
from mbpp_152_code import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(merge_sort([3, 2, 1, 5, 4]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_already_sorted(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(merge_sort([1, 2, 2, 3, 4]), [1, 2, 2, 3, 4])

    def test_negative_numbers(self):
        self.assertEqual(merge_sort([-5, -3, -1, 0, 2]), [-5, -3, -1, 0, 2])

    def test_large_numbers(self):
        self.assertEqual(merge_sort([100, 200, 150, 300, 250]), [100, 150, 200, 250, 300])

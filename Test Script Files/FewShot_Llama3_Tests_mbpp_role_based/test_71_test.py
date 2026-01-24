import unittest
from mbpp_71_code import comb_sort

class TestCombSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(comb_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(comb_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(comb_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(comb_sort([5, 2, 8, 3, 1, 4, 6, 7]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_list_with_duplicates(self):
        self.assertEqual(comb_sort([5, 2, 8, 3, 3, 1, 4, 6, 7]), [1, 2, 3, 3, 4, 5, 6, 7, 8])

    def test_list_with_negative_numbers(self):
        self.assertEqual(comb_sort([-5, 2, -8, 3, 1, -4, 6, 7]), [-8, -5, -4, 1, 2, 3, 6, 7])

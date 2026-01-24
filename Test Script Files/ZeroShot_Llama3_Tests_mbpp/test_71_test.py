import unittest
from mbpp_71_code import comb_sort

class TestCombSort(unittest.TestCase):

    def test_comb_sort_empty_list(self):
        self.assertEqual(comb_sort([]), [])

    def test_comb_sort_single_element_list(self):
        self.assertEqual(comb_sort([5]), [5])

    def test_comb_sort_already_sorted_list(self):
        self.assertEqual(comb_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_comb_sort_reverse_sorted_list(self):
        self.assertEqual(comb_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_comb_sort_unsorted_list(self):
        self.assertEqual(comb_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

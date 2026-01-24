import unittest
from mbpp_71_code import comb_sort

class TestCombSort(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(comb_sort([]), [])

    def test_single_element_input(self):
        self.assertEqual(comb_sort([5]), [5])

    def test_sorted_input(self):
        self.assertEqual(comb_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_input(self):
        self.assertEqual(comb_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_input(self):
        self.assertEqual(comb_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_duplicates_input(self):
        self.assertEqual(comb_sort([5, 2, 8, 2, 4, 1, 3, 1]), [1, 1, 2, 2, 3, 4, 5, 8])

    def test_large_input(self):
        self.assertEqual(comb_sort([5, 2, 8, 2, 4, 1, 3, 1, 9, 7, 6, 5, 4, 3, 2, 1]), [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9])

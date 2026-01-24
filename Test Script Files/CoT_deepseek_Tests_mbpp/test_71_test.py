import unittest
from mbpp_71_code import comb_sort

class TestCombSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(comb_sort([5, 3, 2, 1, 6]), [1, 2, 3, 5, 6])

    def test_already_sorted(self):
        self.assertEqual(comb_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_single_element(self):
        self.assertEqual(comb_sort([5]), [5])

    def test_empty_list(self):
        self.assertEqual(comb_sort([]), [])

    def test_negative_numbers(self):
        self.assertEqual(comb_sort([-5, -3, -2, -1, -6]), [-6, -5, -3, -2, -1])

    def test_duplicate_elements(self):
        self.assertEqual(comb_sort([5, 3, 2, 1, 6, 6]), [1, 2, 3, 5, 6, 6])

    def test_large_numbers(self):
        self.assertEqual(comb_sort(list(range(1000, 0, -1))), list(range(1, 1001)))

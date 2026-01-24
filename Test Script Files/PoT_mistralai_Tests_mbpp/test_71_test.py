import unittest
from mbpp_71_code import comb_sort

class TestCombSort(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(comb_sort([5, 3, 8, 4, 2, 9, 1, 7, 6]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(comb_sort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(comb_sort([-1, -5, 0, 3, 10]), [-1, -5, 0, 3, 10])

    def test_edge_case_single_element(self):
        self.assertEqual(comb_sort([1]), [1])

    def test_edge_case_empty_list(self):
        self.assertEqual(comb_sort([]), [])

    def test_edge_case_duplicates(self):
        self.assertEqual(comb_sort([1, 1, 1]), [1, 1, 1])

    def test_edge_case_reverse_order(self):
        self.assertEqual(comb_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_all_same(self):
        self.assertEqual(comb_sort([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(comb_sort([-5, -3, -1, 0, 1, 3, 5]), [-5, -3, -1, 0, 1, 3, 5])

    def test_edge_case_large_numbers(self):
        self.assertEqual(comb_sort([100000, 99999, 99998, 1, 2, 3, 4]), [1, 2, 3, 4, 99998, 99999, 100000])

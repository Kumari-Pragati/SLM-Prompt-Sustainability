import unittest
from mbpp_71_code import comb_sort

class TestCombSort(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(comb_sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])

    def test_edge_case_empty_list(self):
        self.assertEqual(comb_sort([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(comb_sort([5]), [5])

    def test_edge_case_sorted_list(self):
        self.assertEqual(comb_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_reverse_sorted_list(self):
        self.assertEqual(comb_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_edge_case_duplicates(self):
        self.assertEqual(comb_sort([5, 2, 4, 2, 1, 3, 1]), [1, 1, 2, 2, 3, 4, 5])

    def test_edge_case_duplicates_sorted(self):
        self.assertEqual(comb_sort([1, 2, 2, 3, 4, 5]), [1, 2, 2, 3, 4, 5])

    def test_edge_case_duplicates_reverse_sorted(self):
        self.assertEqual(comb_sort([5, 4, 3, 2, 2, 1, 1]), [1, 1, 2, 2, 3, 4, 5])

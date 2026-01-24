import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(pancake_sort([3, 2, 1]), [1, 2, 3])

    def test_edge_case_empty_list(self):
        self.assertEqual(pancake_sort([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(pancake_sort([1]), [1])

    def test_edge_case_reverse_sorted_list(self):
        self.assertEqual(pancake_sort([3, 2, 1, 4]), [1, 2, 3, 4])

    def test_edge_case_already_sorted_list(self):
        self.assertEqual(pancake_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_edge_case_duplicates_list(self):
        self.assertEqual(pancake_sort([2, 2, 1, 1]), [1, 1, 2, 2])

    def test_edge_case_negative_numbers_list(self):
        self.assertEqual(pancake_sort([-3, -2, -1]), [-1, -2, -3])

    def test_edge_case_mixed_positive_and_negative_numbers_list(self):
        self.assertEqual(pancake_sort([-3, 2, -2, 1]), [-3, -2, 1, 2])

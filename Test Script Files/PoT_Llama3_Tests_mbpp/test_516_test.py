import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]), [2, 24, 45, 66, 75, 80, 90, 170])

    def test_edge_case_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(radix_sort([5]), [5])

    def test_edge_case_all_equal_elements_list(self):
        self.assertEqual(radix_sort([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_edge_case_all_distinct_elements_list(self):
        self.assertEqual(radix_sort([5, 2, 8, 12, 1, 9]), [1, 2, 5, 8, 9, 12])

    def test_edge_case_negative_elements_list(self):
        self.assertEqual(radix_sort([-5, -2, -8, -12, -1, -9]), [-12, -9, -8, -5, -2, -1])

    def test_edge_case_mixed_negative_positive_elements_list(self):
        self.assertEqual(radix_sort([-5, 2, -8, 12, -1, 9]), [-12, -8, -5, -1, 2, 9])

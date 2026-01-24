import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(radix_sort([3, 2, 9, 7, 5, 1, 4, 6, 8]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_single_element(self):
        self.assertEqual(radix_sort([5]), [5])

    def test_edge_case_sorted_list(self):
        self.assertEqual(radix_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_reverse_sorted_list(self):
        self.assertEqual(radix_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(radix_sort([-5, -3, -1, -9, -7]), [-9, -7, -5, -3, -1])

    def test_corner_case_mixed_positive_negative(self):
        self.assertEqual(radix_sort([3, -1, 2, -5, 4]), [-5, -1, 2, 3, 4])

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(radix_sort([5, 5, 1, 1, 2, 2]), [1, 1, 2, 2, 5, 5])

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            radix_sort([1, 2, '3', 4, 5])

    def test_invalid_input_mixed_types(self):
        with self.assertRaises(TypeError):
            radix_sort([1, '2', 3, 4, '5'])

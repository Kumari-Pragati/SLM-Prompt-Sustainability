import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(radix_sort([329, 457, 657, 832, 435, 726, 333]), [329, 333, 435, 457, 657, 726, 832])

    def test_edge_case_single_element(self):
        self.assertEqual(radix_sort([5]), [5])

    def test_boundary_case_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_boundary_case_negative_numbers(self):
        self.assertEqual(radix_sort([-3, -1, -4]), [-4, -3, -1])

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            radix_sort([1, 2, '3'])

    def test_invalid_input_mixed_types(self):
        with self.assertRaises(TypeError):
            radix_sort([1, '2', 3])

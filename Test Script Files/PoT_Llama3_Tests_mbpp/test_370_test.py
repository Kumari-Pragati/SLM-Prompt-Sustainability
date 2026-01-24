import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(float_sort([[1, 'a'], [2, 'b'], [3, 'c']]), [[3, 'c'], [2, 'b'], [1, 'a']])

    def test_edge_case_reverse(self):
        self.assertEqual(float_sort([[1, 'a'], [2, 'b'], [3, 'c']], reverse=False), [[1, 'a'], [2, 'b'], [3, 'c']])

    def test_edge_case_empty_list(self):
        self.assertEqual(float_sort([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(float_sort([[1, 'a']]), [[1, 'a']])

    def test_edge_case_single_element_list_reverse(self):
        self.assertEqual(float_sort([[1, 'a']], reverse=True), [[1, 'a']])

    def test_edge_case_single_element_list_reverse_empty(self):
        self.assertEqual(float_sort([], reverse=True), [])

    def test_edge_case_single_element_list_reverse_single_element(self):
        self.assertEqual(float_sort([[1, 'a']], reverse=True), [[1, 'a']])

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            float_sort('invalid_input')

import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDnf(unittest.TestCase):
    def test_typical_input(self):
        arr = [0, 1, 1, 0, 1, 0, 1]
        n = len(arr)
        result = sort_by_dnf(arr, n)
        expected = [0, 0, 0, 0, 1, 1, 1]
        self.assertEqual(result, expected)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        result = sort_by_dnf(arr, n)
        expected = []
        self.assertEqual(result, expected)

    def test_edge_case_single_element_array(self):
        arr = [0]
        n = len(arr)
        result = sort_by_dnf(arr, n)
        expected = [0]
        self.assertEqual(result, expected)

    def test_edge_case_all_zeros_array(self):
        arr = [0, 0, 0, 0, 0, 0, 0]
        n = len(arr)
        result = sort_by_dnf(arr, n)
        expected = [0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result, expected)

    def test_edge_case_all_ones_array(self):
        arr = [1, 1, 1, 1, 1, 1, 1]
        n = len(arr)
        result = sort_by_dnf(arr, n)
        expected = [1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(result, expected)

    def test_invalid_input_non_integer_n(self):
        arr = [0, 1, 1, 0, 1, 0, 1]
        n = 'abc'
        with self.assertRaises(TypeError):
            sort_by_dnf(arr, n)

    def test_invalid_input_non_list_input(self):
        arr = 'abc'
        n = len(arr)
        with self.assertRaises(TypeError):
            sort_by_dnf(arr, n)

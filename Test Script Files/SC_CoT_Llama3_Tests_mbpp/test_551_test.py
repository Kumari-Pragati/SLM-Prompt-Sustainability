import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):

    def test_typical_inputs(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        result = extract_column(list1, n)
        self.assertEqual(result, [3, 6, 9])

    def test_edge_case_empty_list(self):
        list1 = []
        n = 0
        result = extract_column(list1, n)
        self.assertEqual(result, [])

    def test_edge_case_single_element_list(self):
        list1 = [[1, 2, 3]]
        n = 0
        result = extract_column(list1, n)
        self.assertEqual(result, [3])

    def test_edge_case_negative_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = -1
        with self.assertRaises(IndexError):
            extract_column(list1, n)

    def test_edge_case_out_of_range_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 3
        with self.assertRaises(IndexError):
            extract_column(list1, n)

    def test_edge_case_zero_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 0
        result = extract_column(list1, n)
        self.assertEqual(result, [3, 6, 9])

    def test_edge_case_list_of_lists_with_zero_elements(self):
        list1 = [[], [], []]
        n = 0
        result = extract_column(list1, n)
        self.assertEqual(result, [])

    def test_edge_case_list_of_lists_with_one_element(self):
        list1 = [[1], [2], [3]]
        n = 0
        result = extract_column(list1, n)
        self.assertEqual(result, [1, 2, 3])

    def test_edge_case_list_of_lists_with_multiple_elements(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 0
        result = extract_column(list1, n)
        self.assertEqual(result, [3, 6, 9])

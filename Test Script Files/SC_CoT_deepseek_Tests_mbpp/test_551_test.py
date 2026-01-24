import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):

    def test_typical_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        expected_output = [2, 5, 8]
        self.assertEqual(extract_column(list1, n), expected_output)

    def test_edge_case_smallest_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 0
        expected_output = [1, 4, 7]
        self.assertEqual(extract_column(list1, n), expected_output)

    def test_edge_case_largest_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 2
        expected_output = [3, 6, 9]
        self.assertEqual(extract_column(list1, n), expected_output)

    def test_corner_case_empty_list(self):
        list1 = []
        n = 0
        expected_output = []
        self.assertEqual(extract_column(list1, n), expected_output)

    def test_invalid_input_negative_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = -1
        with self.assertRaises(IndexError):
            extract_column(list1, n)

    def test_invalid_input_large_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 3
        with self.assertRaises(IndexError):
            extract_column(list1, n)

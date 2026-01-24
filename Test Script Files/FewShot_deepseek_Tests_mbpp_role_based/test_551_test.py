import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        self.assertEqual(extract_column(list1, n), [2, 5, 8])

    def test_edge_case_first_column(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 0
        self.assertEqual(extract_column(list1, n), [1, 4, 7])

    def test_edge_case_last_column(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 2
        self.assertEqual(extract_column(list1, n), [3, 6, 9])

    def test_boundary_case_single_element(self):
        list1 = [[1]]
        n = 0
        self.assertEqual(extract_column(list1, n), [1])

    def test_boundary_case_empty_list(self):
        list1 = []
        n = 0
        self.assertEqual(extract_column(list1, n), [])

    def test_invalid_input_negative_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = -1
        with self.assertRaises(IndexError):
            extract_column(list1, n)

    def test_invalid_input_out_of_range_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 3
        with self.assertRaises(IndexError):
            extract_column(list1, n)

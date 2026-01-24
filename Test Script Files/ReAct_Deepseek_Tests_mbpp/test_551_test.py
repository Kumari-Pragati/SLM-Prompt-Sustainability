import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):

    def test_typical_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        expected_result = [2, 5, 8]
        self.assertEqual(extract_column(list1, n), expected_result)

    def test_edge_case_empty_list(self):
        list1 = []
        n = 0
        expected_result = []
        self.assertEqual(extract_column(list1, n), expected_result)

    def test_edge_case_single_element_list(self):
        list1 = [[1]]
        n = 0
        expected_result = [1]
        self.assertEqual(extract_column(list1, n), expected_result)

    def test_error_case_negative_index(self):
        list1 = [[1, 2, 3]]
        n = -1
        with self.assertRaises(IndexError):
            extract_column(list1, n)

    def test_error_case_out_of_range_index(self):
        list1 = [[1, 2, 3]]
        n = 3
        with self.assertRaises(IndexError):
            extract_column(list1, n)

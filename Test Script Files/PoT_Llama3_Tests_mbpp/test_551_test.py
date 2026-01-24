import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):
    def test_typical_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        expected = [2, 5, 8]
        self.assertEqual(extract_column(list1, n), expected)

    def test_edge_case_empty_list(self):
        list1 = []
        n = 0
        expected = []
        self.assertEqual(extract_column(list1, n), expected)

    def test_edge_case_single_element_list(self):
        list1 = [[1, 2, 3]]
        n = 0
        expected = [3]
        self.assertEqual(extract_column(list1, n), expected)

    def test_edge_case_negative_n(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = -1
        expected = []
        self.assertEqual(extract_column(list1, n), expected)

    def test_edge_case_out_of_bounds_n(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 3
        expected = []
        self.assertEqual(extract_column(list1, n), expected)

    def test_edge_case_list_with_single_element(self):
        list1 = [[1, 2, 3]]
        n = 2
        expected = [3]
        self.assertEqual(extract_column(list1, n), expected)

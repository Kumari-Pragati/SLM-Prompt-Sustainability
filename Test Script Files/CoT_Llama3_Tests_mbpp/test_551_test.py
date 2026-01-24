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
        n = 1
        expected = []
        self.assertEqual(extract_column(list1, n), expected)

    def test_edge_case_single_element_list(self):
        list1 = [[1, 2, 3]]
        n = 1
        expected = [2]
        self.assertEqual(extract_column(list1, n), expected)

    def test_edge_case_invalid_input_type(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 'a'
        with self.assertRaises(TypeError):
            extract_column(list1, n)

    def test_edge_case_invalid_input_value(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 10
        with self.assertRaises(IndexError):
            extract_column(list1, n)

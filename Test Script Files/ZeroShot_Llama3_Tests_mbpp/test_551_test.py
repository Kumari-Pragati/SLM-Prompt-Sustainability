import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):

    def test_extract_column(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        expected_result = [2, 5, 8]
        self.assertEqual(extract_column(list1, n), expected_result)

    def test_extract_column_empty_list(self):
        list1 = []
        n = 1
        expected_result = []
        self.assertEqual(extract_column(list1, n), expected_result)

    def test_extract_column_empty_sublist(self):
        list1 = [[], [1, 2, 3], [4, 5, 6]]
        n = 1
        expected_result = [2, 5, 6]
        self.assertEqual(extract_column(list1, n), expected_result)

    def test_extract_column_invalid_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 10
        with self.assertRaises(IndexError):
            extract_column(list1, n)

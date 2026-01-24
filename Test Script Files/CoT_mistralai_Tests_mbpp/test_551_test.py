import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):
    def test_empty_list(self):
        self.assertRaises(IndexError, extract_column, [], 0)

    def test_single_list(self):
        self.assertEqual(extract_column([[1, 2, 3], [4, 5, 6]], 0), [1, 4])

    def test_multiple_lists(self):
        self.assertEqual(extract_column([[1, 2, 3], [4, 5, 6]], 1), [2, 5])

    def test_negative_index(self):
        self.assertRaises(IndexError, extract_column, [[1, 2, 3], [4, 5, 6]], -1)

    def test_out_of_range_index(self):
        self.assertRaises(IndexError, extract_column, [[1, 2, 3], [4, 5, 6]], 3)

    def test_list_with_single_element(self):
        self.assertEqual(extract_column([[1]], 0), [1])

    def test_list_with_empty_element(self):
        self.assertEqual(extract_column([[None]], 0), [None])

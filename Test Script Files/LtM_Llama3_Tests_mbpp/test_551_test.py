import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(extract_column([], 0), [])

    def test_single_element_list(self):
        self.assertEqual(extract_column([[1, 2, 3]], 0), [3])

    def test_multiple_elements_list(self):
        self.assertEqual(extract_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [2, 5, 8])

    def test_list_with_zero_index(self):
        self.assertEqual(extract_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0), [3, 6, 9])

    def test_list_with_max_index(self):
        self.assertEqual(extract_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), [3, 6, 9])

    def test_list_with_invalid_index(self):
        with self.assertRaises(IndexError):
            extract_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3)

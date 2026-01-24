import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_matrix([]), [])

    def test_single_element(self):
        self.assertEqual(sort_matrix([[1]]), [[1]])

    def test_single_row(self):
        self.assertEqual(sort_matrix([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_single_column(self):
        self.assertEqual(sort_matrix([[1, 2], [3, 1]]), [[1, 3], [2, 1]])

    def test_mixed_rows_columns(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_matrix_with_duplicates(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [2, 1, 2], [3, 2, 1]]), [[1, 2, 3], [2, 1, 2], [3, 2, 1]])

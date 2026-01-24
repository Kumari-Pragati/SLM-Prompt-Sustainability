import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(sort_matrix([]), [])

    def test_single_row_matrix(self):
        self.assertEqual(sort_matrix([[1, 2, 3]]), [[1, 2, 3]])

    def test_single_column_matrix(self):
        self.assertEqual(sort_matrix([[1], [2], [3]]), [[1, 2, 3]])

    def test_sorted_matrix(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_unsorted_matrix(self):
        self.assertEqual(sort_matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_matrix_with_duplicates(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [4, 4, 5], [6, 7, 8]]), [[1, 2, 3], [4, 4, 5], [6, 7, 8]])

    def test_matrix_with_negative_numbers(self):
        self.assertEqual(sort_matrix([[-1, 0, 1], [2, -3, 4], [5, 6, -7]]), [[-7, -3, 0], [1, 2, 4], [5, 6]])

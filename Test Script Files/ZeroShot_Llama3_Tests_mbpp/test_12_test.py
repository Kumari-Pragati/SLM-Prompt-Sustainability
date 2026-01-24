import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):
    def test_sort_matrix(self):
        M = [[4, 2, 1], [3, 5, 6], [7, 8, 9]]
        expected = [[1, 2, 4], [3, 5, 6], [7, 8, 9]]
        self.assertEqual(sort_matrix(M), expected)

        M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(sort_matrix(M), expected)

        M = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(sort_matrix(M), expected)

    def test_sort_matrix_empty(self):
        M = []
        expected = []
        self.assertEqual(sort_matrix(M), expected)

    def test_sort_matrix_single_row(self):
        M = [[1, 2, 3]]
        expected = [[1, 2, 3]]
        self.assertEqual(sort_matrix(M), expected)

    def test_sort_matrix_single_column(self):
        M = [[1], [2], [3]]
        expected = [[1], [2], [3]]
        self.assertEqual(sort_matrix(M), expected)

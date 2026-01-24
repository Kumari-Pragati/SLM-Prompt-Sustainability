import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):
    def test_sorted_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        sorted_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(sort_matrix(matrix), sorted_matrix)

    def test_empty_matrix(self):
        matrix = []
        self.assertEqual(sort_matrix(matrix), [])

    def test_single_row_matrix(self):
        matrix = [[1]]
        sorted_matrix = [[1]]
        self.assertEqual(sort_matrix(matrix), sorted_matrix)

    def test_single_column_matrix(self):
        matrix = [[1], [2], [3]]
        sorted_matrix = [[1], [2], [3]]
        self.assertEqual(sort_matrix(matrix), sorted_matrix)

    def test_matrix_with_duplicates(self):
        matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        sorted_matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        self.assertEqual(sort_matrix(matrix), sorted_matrix)

    def test_matrix_with_negative_numbers(self):
        matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        sorted_matrix = [[-9, -8, -7], [-6, -5, -4], [-3, -2, -1]]
        self.assertEqual(sort_matrix(matrix), sorted_matrix)

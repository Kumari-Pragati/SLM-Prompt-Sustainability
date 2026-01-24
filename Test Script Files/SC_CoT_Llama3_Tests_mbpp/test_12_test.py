import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):
    def test_typical_input(self):
        M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = sort_matrix(M)
        self.assertEqual(result, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_edge_case_empty_matrix(self):
        M = []
        result = sort_matrix(M)
        self.assertEqual(result, [])

    def test_edge_case_single_row_matrix(self):
        M = [[1, 2, 3]]
        result = sort_matrix(M)
        self.assertEqual(result, [[1, 2, 3]])

    def test_edge_case_single_column_matrix(self):
        M = [[1], [2], [3]]
        result = sort_matrix(M)
        self.assertEqual(result, [[1], [2], [3]])

    def test_edge_case_matrix_with_duplicates(self):
        M = [[1, 2, 3], [4, 4, 6], [7, 8, 9]]
        result = sort_matrix(M)
        self.assertEqual(result, [[1, 2, 3], [4, 4, 6], [7, 8, 9]])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sort_matrix("not a matrix")

    def test_invalid_input_non_matrix(self):
        M = "not a matrix"
        with self.assertRaises(TypeError):
            sort_matrix(M)

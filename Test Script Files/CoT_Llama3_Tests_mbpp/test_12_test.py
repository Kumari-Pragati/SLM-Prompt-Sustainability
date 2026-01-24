import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):

    def test_typical_input(self):
        M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(sort_matrix(M), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_edge_case_empty_matrix(self):
        M = []
        self.assertEqual(sort_matrix(M), [])

    def test_edge_case_single_row_matrix(self):
        M = [[1, 2, 3]]
        self.assertEqual(sort_matrix(M), [[1, 2, 3]])

    def test_edge_case_single_column_matrix(self):
        M = [[1], [2], [3]]
        self.assertEqual(sort_matrix(M), [[1], [2], [3]])

    def test_edge_case_single_element_matrix(self):
        M = [[1]]
        self.assertEqual(sort_matrix(M), [[1]])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sort_matrix("Invalid input")

    def test_invalid_input_non_matrix(self):
        M = "Invalid input"
        with self.assertRaises(TypeError):
            sort_matrix(M)

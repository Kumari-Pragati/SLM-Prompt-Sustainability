import unittest
from mbpp_652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):
    def test_matrix_to_list(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], [4, 5, 6]]), '[(1, 2, 3), (4, 5, 6)]')
        self.assertEqual(matrix_to_list([[1, 2], [3, 4], [5, 6]]), '[(1, 3, 5), (2, 4, 6)]')
        self.assertEqual(matrix_to_list([[1, 2, 3, 4], [5, 6, 7, 8]]), '[(1, 5), (2, 6), (3, 7), (4, 8)]')
        self.assertEqual(matrix_to_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), '[(1, 4, 7), (2, 5, 8), (3, 6, 9)]')
        self.assertEqual(matrix_to_list([[1, 2], [3, 4]]), '[(1, 3), (2, 4)]')
        self.assertEqual(matrix_to_list([[1, 2, 3, 4, 5, 6, 7, 8, 9]]), '[(1, 2, 3, 4, 5, 6, 7, 8, 9)]')

    def test_empty_matrix(self):
        self.assertEqual(matrix_to_list([]), '[]')

    def test_single_row_matrix(self):
        self.assertEqual(matrix_to_list([[1, 2, 3]]), '[(1, 2, 3)]')

    def test_single_column_matrix(self):
        self.assertEqual(matrix_to_list([[1], [2], [3]]), '[(1,), (2,), (3,)]')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            matrix_to_list('not a list')

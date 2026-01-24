import unittest
from mbpp_652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], [4, 5, 6]]), '[(1, 4), (2, 5), (3, 6)]')

    def test_empty_input(self):
        self.assertEqual(matrix_to_list([]), '[]')

    def test_single_row_input(self):
        self.assertEqual(matrix_to_list([[1, 2, 3]]), '[(1,), (2,), (3,)]')

    def test_single_column_input(self):
        self.assertEqual(matrix_to_list([[1], [2], [3]]), '[(1,), (2,), (3,)]')

    def test_empty_row_input(self):
        self.assertEqual(matrix_to_list([[], [1, 2, 3]]), '[]')

    def test_empty_column_input(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], []]), '[]')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            matrix_to_list('invalid input')

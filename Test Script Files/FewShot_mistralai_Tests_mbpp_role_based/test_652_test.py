import unittest
from mbpp_652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):
    def test_valid_matrix(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), '["[1, 2, 3]", "[4, 5, 6]", "[7, 8, 9]"')

    def test_empty_matrix(self):
        self.assertEqual(matrix_to_list([]), '[]')

    def test_single_row_matrix(self):
        self.assertEqual(matrix_to_list([[1, 2, 3]]), '["[1, 2, 3]"]')

    def test_single_column_matrix(self):
        self.assertEqual(matrix_to_list([[1], [2], [3]]), '["[1]", "[2]", "[3]"]')

    def test_mixed_row_column_matrix(self):
        self.assertEqual(matrix_to_list([[1], [2, 3], [4, 5, 6]]), '["[1]", "[2, 3]", "[4, 5, 6]"]')

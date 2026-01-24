import unittest
from mbpp_652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(matrix_to_list([]), '[]')

    def test_single_element_list(self):
        self.assertEqual(matrix_to_list([[1]]), '[1]')

    def test_single_row_matrix(self):
        self.assertEqual(matrix_to_list([[1, 2, 3]]), '[1, 2, 3]')

    def test_single_column_matrix(self):
        self.assertEqual(matrix_to_list([[1], [2], [3]]), '[1, 2, 3]')

    def test_multi_row_multi_column_matrix(self):
        self.assertEqual(matrix_to_list([[1, 2], [3, 4]]), '[1, 3, 2, 4]')

    def test_mixed_row_column_matrix(self):
        self.assertEqual(matrix_to_list([[1], [2, 3], [4, 5, 6]]), '[1, 2, 4, 3, 5, 6]')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            matrix_to_list(123)

    def test_invalid_input_format(self):
        with self.assertRaises(ValueError):
            matrix_to_list([[1, 2], [3]])

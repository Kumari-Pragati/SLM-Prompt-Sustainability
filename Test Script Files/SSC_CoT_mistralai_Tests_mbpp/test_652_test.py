import unittest
from mbpp_652_code import zip
from 652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):

    def test_matrix_to_list_normal(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), '["[1, 4, 7]", "[2, 5, 8]", "[3, 6, 9]"]')

    def test_matrix_to_list_edge_cases(self):
        self.assertEqual(matrix_to_list([[1], [2]]), '["[1]", "[2]"]')
        self.assertEqual(matrix_to_list([[1, 2], [3, 4], [5, 6]]), '["[1, 3, 5]", "[2, 4, 6]"]')
        self.assertEqual(matrix_to_list([[1, 2, 3], [4], [5, 6, 7]]), '["[1, 4, 5]", "[2, 6, 7]"]')
        self.assertEqual(matrix_to_list([[]]), '["[]"]')

    def test_matrix_to_list_empty(self):
        self.assertEqual(matrix_to_list([]), '["[]"]')

    def test_matrix_to_list_invalid_input(self):
        with self.assertRaises(TypeError):
            matrix_to_list('not a list')
        with self.assertRaises(TypeError):
            matrix_to_list([1, 2, 3])

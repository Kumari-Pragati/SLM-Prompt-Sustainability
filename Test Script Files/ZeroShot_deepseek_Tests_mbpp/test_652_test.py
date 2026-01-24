import unittest
from mbpp_652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(matrix_to_list([[1]]), '((1,))')

    def test_multiple_elements(self):
        self.assertEqual(matrix_to_list([[1, 2], [3, 4]]), '((1, 3), (2, 4))')

    def test_empty_matrix(self):
        self.assertEqual(matrix_to_list([[]]), '()')

    def test_empty_elements(self):
        self.assertEqual(matrix_to_list([[], []]), '()')

    def test_single_row(self):
        self.assertEqual(matrix_to_list([[1, 2, 3]]), '((1, 2, 3),)')

    def test_single_column(self):
        self.assertEqual(matrix_to_list([[1], [2], [3]]), '((1,), (2,), (3,))')

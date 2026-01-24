import unittest
from mbpp_652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(matrix_to_list([[1, 2], [3, 4]]), '((1, 2), (3, 4))')

    def test_empty_input(self):
        self.assertEqual(matrix_to_list([]), '()')

    def test_single_element_input(self):
        self.assertEqual(matrix_to_list([[5]]), '((5,),)')

    def test_multiple_single_element_rows(self):
        self.assertEqual(matrix_to_list([[1], [2], [3]]), '((1,), (2,), (3,))')

    def test_edge_values(self):
        self.assertEqual(matrix_to_list([[-1, 0], [1, 255]]), '((-1, 0), (1, 255))')

    def test_complex_input(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), '((1, 2, 3), (4, 5, 6), (7, 8, 9))')

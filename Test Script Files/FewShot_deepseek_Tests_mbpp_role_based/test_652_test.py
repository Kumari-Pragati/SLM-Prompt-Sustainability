import unittest
from mbpp_652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(matrix_to_list(test_list), '((1, 4, 7), (2, 5, 8), (3, 6, 9))')

    def test_empty_matrix(self):
        test_list = []
        self.assertEqual(matrix_to_list(test_list), '()')

    def test_single_element_matrix(self):
        test_list = [[1]]
        self.assertEqual(matrix_to_list(test_list), '((1,),)')

    def test_two_by_two_matrix(self):
        test_list = [[1, 2], [3, 4]]
        self.assertEqual(matrix_to_list(test_list), '((1, 3), (2, 4))')

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            matrix_to_list(123)

import unittest
from mbpp_652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(matrix_to_list([[1, 2], [3, 4]]), '[[1, 3], [2, 4]]')

    def test_empty_list(self):
        self.assertEqual(matrix_to_list([]), '[]')

    def test_single_element_list(self):
        self.assertEqual(matrix_to_list([[1]]), '[[1]]')

    def test_list_with_single_element(self):
        self.assertEqual(matrix_to_list([[1]]), '[[1]]')

    def test_list_with_different_lengths(self):
        self.assertEqual(matrix_to_list([[1, 2], [3]]), '[[1, 3], [2]]')

    def test_list_with_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            matrix_to_list([[1, 'a'], [2, 'b']])

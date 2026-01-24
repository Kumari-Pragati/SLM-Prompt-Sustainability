import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquareTest(unittest.TestCase):

    def test_typical_case(self):
        matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        self.assertTrue(magic_square_test(matrix))

    def test_empty_matrix(self):
        matrix = []
        self.assertTrue(magic_square_test(matrix))

    def test_single_element_matrix(self):
        matrix = [[5]]
        self.assertTrue(magic_square_test(matrix))

    def test_invalid_matrix(self):
        matrix = [[2, 7, 6], [9, 5], [4, 3, 8]]
        self.assertFalse(magic_square_test(matrix))

    def test_invalid_matrix_with_non_integer_elements(self):
        matrix = [[2, 7, 'a'], [9, 5, 1], [4, 3, 8]]
        with self.assertRaises(TypeError):
            magic_square_test(matrix)

    def test_invalid_matrix_with_non_list_elements(self):
        matrix = [2, 7, 6]
        with self.assertRaises(TypeError):
            magic_square_test(matrix)

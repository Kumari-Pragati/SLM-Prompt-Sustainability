import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquareTest(unittest.TestCase):
    def test_typical_case(self):
        matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        self.assertTrue(magic_square_test(matrix))

    def test_edge_case(self):
        matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertTrue(magic_square_test(matrix))

    def test_boundary_case(self):
        matrix = [[1]]
        self.assertTrue(magic_square_test(matrix))

    def test_invalid_input(self):
        matrix = [[1, 2, 3], [4, 5, 6], 'a']
        with self.assertRaises(TypeError):
            magic_square_test(matrix)

    def test_invalid_matrix_size(self):
        matrix = [[1, 2, 3], [4, 5]]
        self.assertFalse(magic_square_test(matrix))

    def test_non_square_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6, 7]]
        self.assertFalse(magic_square_test(matrix))

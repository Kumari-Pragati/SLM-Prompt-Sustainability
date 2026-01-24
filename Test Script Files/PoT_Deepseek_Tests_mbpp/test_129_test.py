import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquareTest(unittest.TestCase):

    def test_typical_case(self):
        matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        self.assertTrue(magic_square_test(matrix))

    def test_edge_case_with_single_row(self):
        matrix = [[1, 2, 3, 4, 5]]
        self.assertTrue(magic_square_test(matrix))

    def test_edge_case_with_single_column(self):
        matrix = [[1], [2], [3], [4], [5]]
        self.assertTrue(magic_square_test(matrix))

    def test_edge_case_with_single_element(self):
        matrix = [[5]]
        self.assertTrue(magic_square_test(matrix))

    def test_corner_case_with_empty_matrix(self):
        matrix = []
        self.assertTrue(magic_square_test(matrix))

    def test_corner_case_with_non_square_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertFalse(magic_square_test(matrix))

    def test_corner_case_with_non_integer_elements(self):
        matrix = [['2', '7', '6'], ['9', '5', '1'], ['4', '3', '8']]
        self.assertFalse(magic_square_test(matrix))

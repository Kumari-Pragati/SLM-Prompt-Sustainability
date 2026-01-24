import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):
    def test_valid_magic_square(self):
        matrix = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        self.assertTrue(magic_square_test(matrix))

    def test_invalid_magic_square(self):
        matrix = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5, 0]
        ]
        self.assertFalse(magic_square_test(matrix))

    def test_empty_matrix(self):
        matrix = []
        self.assertFalse(magic_square_test(matrix))

    def test_single_row_matrix(self):
        matrix = [
            [1, 2, 3]
        ]
        self.assertFalse(magic_square_test(matrix))

    def test_single_column_matrix(self):
        matrix = [
            [1],
            [2],
            [3]
        ]
        self.assertFalse(magic_square_test(matrix))

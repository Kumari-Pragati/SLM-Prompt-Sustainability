import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):
    def test_valid_magic_square(self):
        square_1 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
        self.assertTrue(magic_square_test(square_1))

    def test_empty_matrix(self):
        empty_matrix = []
        self.assertFalse(magic_square_test(empty_matrix))

    def test_single_row_matrix(self):
        single_row = [[1, 2, 3]]
        self.assertFalse(magic_square_test(single_row))

    def test_single_column_matrix(self):
        single_column = [[1], [2], [3]]
        self.assertFalse(magic_square_test(single_column))

    def test_non_square_matrix(self):
        non_square = [[1, 2, 3], [4, 5], [6, 7, 8]]
        self.assertFalse(magic_square_test(non_square))

    def test_negative_numbers(self):
        negative_numbers = [[-1, 2, 3], [4, -5, 7], [8, 1, -6]]
        self.assertFalse(magic_square_test(negative_numbers))

    def test_zero_numbers(self):
        zero_numbers = [[0, 2, 3], [4, 0, 7], [8, 1, 0]]
        self.assertFalse(magic_square_test(zero_numbers))

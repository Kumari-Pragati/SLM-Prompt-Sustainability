import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):
    def test_simple_magic_square(self):
        self.assertTrue(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))

    def test_transposed_magic_square(self):
        self.assertTrue(magic_square_test([[1, 8, 7], [2, 9, 6], [3, 4, 5]]))

    def test_symmetric_magic_square(self):
        self.assertTrue(magic_square_test([[1, 5, 9], [5, 5, 5], [9, 5, 1]]))

    def test_empty_matrix(self):
        self.assertFalse(magic_square_test([]))
        self.assertFalse(magic_square_test([[]]))
        self.assertFalse(magic_square_test([[None]]))

    def test_single_row_matrix(self):
        self.assertFalse(magic_square_test([[1]]))
        self.assertFalse(magic_square_test([[1, 2]]))
        self.assertFalse(magic_square_test([[1, 2, 3], [4, 5, 6]]))

    def test_single_column_matrix(self):
        self.assertFalse(magic_square_test([[1], [2], [3]]))
        self.assertFalse(magic_square_test([[1, 2], [3, 4], [5, 6]]))

    def test_non_square_matrix(self):
        self.assertFalse(magic_square_test([[1, 2], [3, 4], [5, 6, 7]]))
        self.assertFalse(magic_square_test([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

    def test_magic_square_with_non_unique_sums(self):
        self.assertFalse(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertFalse(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))

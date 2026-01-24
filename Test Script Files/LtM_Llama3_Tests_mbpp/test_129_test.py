import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):
    def test_valid_magic_square(self):
        self.assertTrue(magic_square_test([[1, 2, 3], [4, 5, 6], [9, 8, 7]]))

    def test_invalid_magic_square(self):
        self.assertFalse(magic_square_test([[1, 2, 3], [4, 5, 6], [8, 7, 9]]))

    def test_empty_magic_square(self):
        self.assertFalse(magic_square_test([]))

    def test_single_row_magic_square(self):
        self.assertFalse(magic_square_test([[1, 2, 3]]))

    def test_single_column_magic_square(self):
        self.assertFalse(magic_square_test([[1], [2], [3]]))

    def test_magic_square_with_duplicates(self):
        self.assertTrue(magic_square_test([[1, 2, 3], [4, 5, 6], [9, 8, 7]]))

    def test_magic_square_with_negative_numbers(self):
        self.assertTrue(magic_square_test([[-1, -2, -3], [-4, -5, -6], [-9, -8, -7]]))

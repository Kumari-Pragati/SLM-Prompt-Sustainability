import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):
    def test_magic_square_normal(self):
        self.assertTrue(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
        self.assertTrue(magic_square_test([[16, 3, 2, 13], [10, 5, 11, 8], [11, 6, 7, 12], [4, 15, 6, 1]]))

    def test_magic_square_edge_cases(self):
        self.assertTrue(magic_square_test([[1], [2], [3]]))
        self.assertTrue(magic_square_test([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
        self.assertTrue(magic_square_test([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]))

    def test_magic_square_invalid_input(self):
        self.assertFalse(magic_square_test([[1, 2], [3]]))
        self.assertFalse(magic_square_test([[1, 2, 3], [4, 5], [6]]))
        self.assertFalse(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
        self.assertFalse(magic_square_test([[1, 2, 3], [4], [5, 6]]))
        self.assertFalse(magic_square_test([[1, 2, 3], [4, 5], [6, 7, 8], [9]]))

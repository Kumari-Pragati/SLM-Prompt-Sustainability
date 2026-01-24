import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):

    def test_magic_square_1x1(self):
        matrix = [[1]]
        self.assertTrue(magic_square_test(matrix))

    def test_magic_square_2x2(self):
        matrix = [[4, 9], [2, 5]]
        self.assertTrue(magic_square_test(matrix))

    def test_magic_square_3x3(self):
        matrix = [[16, 3, 2], [5, 1, 9], [4, 14, 8]]
        self.assertTrue(magic_square_test(matrix))

    def test_magic_square_4x4(self):
        matrix = [[15, 2, 8, 13], [11, 5, 17, 19], [23, 6, 4, 24], [10, 3, 18, 12]]
        self.assertTrue(magic_square_test(matrix))

    def test_magic_square_5x5(self):
        matrix = [[26, 13, 29, 23, 8], [4, 19, 55, 47, 14], [53, 21, 18, 56, 20], [32, 44, 59, 49, 12], [43, 28, 36, 39, 22]]
        self.assertTrue(magic_square_test(matrix))

    def test_non_magic_square_1x1(self):
        matrix = [[10]]
        self.assertFalse(magic_square_test(matrix))

    def test_non_magic_square_2x2(self):
        matrix = [[4, 9], [2, 5]]
        matrix[0][0] = 10
        self.assertFalse(magic_square_test(matrix))

    def test_non_magic_square_3x3(self):
        matrix = [[16, 3, 2], [5, 1, 9], [4, 14, 8]]
        matrix[1][1] = 10
        self.assertFalse(magic_square_test(matrix))

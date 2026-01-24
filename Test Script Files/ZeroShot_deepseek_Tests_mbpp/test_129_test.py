import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):

    def test_magic_square_1(self):
        matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        self.assertTrue(magic_square_test(matrix))

    def test_magic_square_2(self):
        matrix = [[16, 2, 3, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]
        self.assertTrue(magic_square_test(matrix))

    def test_magic_square_3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertFalse(magic_square_test(matrix))

    def test_magic_square_4(self):
        matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertTrue(magic_square_test(matrix))

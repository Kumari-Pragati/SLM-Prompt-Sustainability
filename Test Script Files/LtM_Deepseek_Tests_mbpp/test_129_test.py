import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquareTest(unittest.TestCase):

    def test_simple_magic_square(self):
        matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        self.assertTrue(magic_square_test(matrix))

    def test_empty_matrix(self):
        matrix = []
        self.assertTrue(magic_square_test(matrix))

    def test_single_element_matrix(self):
        matrix = [[5]]
        self.assertTrue(magic_square_test(matrix))

    def test_2x2_magic_square(self):
        matrix = [[4, 9], [3, 5]]
        self.assertTrue(magic_square_test(matrix))

    def test_3x3_magic_square(self):
        matrix = [[16, 2, 3], [5, 10, 11], [9, 8, 6]]
        self.assertTrue(magic_square_test(matrix))

    def test_non_square_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertFalse(magic_square_test(matrix))

    def test_non_magic_square(self):
        matrix = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
        self.assertFalse(magic_square_test(matrix))

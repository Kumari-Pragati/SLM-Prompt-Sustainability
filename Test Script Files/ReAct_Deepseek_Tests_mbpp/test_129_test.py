import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):

    def test_typical_case(self):
        matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        self.assertTrue(magic_square_test(matrix))

    def test_edge_case_3x3(self):
        matrix = [[16, 2, 3], [5, 10, 11], [9, 8, 6]]
        self.assertTrue(magic_square_test(matrix))

    def test_edge_case_2x2(self):
        matrix = [[4, 9], [3, 5]]
        self.assertTrue(magic_square_test(matrix))

    def test_edge_case_1x1(self):
        matrix = [[5]]
        self.assertTrue(magic_square_test(matrix))

    def test_error_case_empty(self):
        matrix = []
        self.assertFalse(magic_square_test(matrix))

    def test_error_case_non_square(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertFalse(magic_square_test(matrix))

    def test_error_case_non_integer(self):
        matrix = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        self.assertFalse(magic_square_test(matrix))

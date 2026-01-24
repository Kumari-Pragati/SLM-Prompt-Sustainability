import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquareTest(unittest.TestCase):
    
    def test_typical_case(self):
        matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        self.assertTrue(magic_square_test(matrix))

    def test_edge_case_3x3(self):
        matrix = [[16, 2, 3], [5, 10, 11], [9, 8, 6]]
        self.assertTrue(magic_square_test(matrix))

    def test_edge_case_4x4(self):
        matrix = [[14, 15, 16, 17], [11, 12, 13, 18], [8, 9, 10, 19], [5, 6, 7, 20]]
        self.assertTrue(magic_square_test(matrix))

    def test_invalid_input(self):
        matrix = [[1, 2, 3], [4, 5, 6], 'a']
        with self.assertRaises(TypeError):
            magic_square_test(matrix)

    def test_invalid_input_empty(self):
        matrix = []
        with self.assertRaises(IndexError):
            magic_square_test(matrix)

    def test_invalid_input_non_square(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertFalse(magic_square_test(matrix))

    def test_invalid_input_non_integer(self):
        matrix = [[1, 2, 3], [4, 'a', 6], [7, 8, 9]]
        with self.assertRaises(TypeError):
            magic_square_test(matrix)

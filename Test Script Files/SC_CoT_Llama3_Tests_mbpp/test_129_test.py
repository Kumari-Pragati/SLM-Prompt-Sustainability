import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):

    def test_typical_input(self):
        my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_edge_case(self):
        my_matrix = [[1, 2], [3, 4]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_edge_case2(self):
        my_matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_edge_case3(self):
        my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_edge_case4(self):
        my_matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_edge_case5(self):
        my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_invalid_input(self):
        my_matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertFalse(magic_square_test(my_matrix))

    def test_invalid_input2(self):
        my_matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        self.assertFalse(magic_square_test(my_matrix))

    def test_invalid_input3(self):
        my_matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
        self.assertFalse(magic_square_test(my_matrix))

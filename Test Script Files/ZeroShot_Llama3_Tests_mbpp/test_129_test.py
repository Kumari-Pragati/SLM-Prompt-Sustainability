import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):

    def test_magic_square_valid(self):
        my_matrix = [[16, 2, 13], [5, 9, 20], [10, 15, 25]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_magic_square_invalid(self):
        my_matrix = [[16, 2, 13], [5, 9, 20], [10, 15, 25], [30, 40, 50]]
        self.assertFalse(magic_square_test(my_matrix))

    def test_magic_square_edge_case1(self):
        my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_magic_square_edge_case2(self):
        my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertFalse(magic_square_test(my_matrix))

    def test_magic_square_edge_case3(self):
        my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
        self.assertFalse(magic_square_test(my_matrix))

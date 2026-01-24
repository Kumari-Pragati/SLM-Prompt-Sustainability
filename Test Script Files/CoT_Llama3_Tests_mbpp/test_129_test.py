import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):

    def test_magic_square_valid(self):
        my_matrix = [[15, 28, 0],
                     [0, 24, 7],
                     [5, 7, 13]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_magic_square_invalid(self):
        my_matrix = [[15, 28, 0],
                     [0, 24, 7],
                     [5, 7, 12]]
        self.assertFalse(magic_square_test(my_matrix))

    def test_magic_square_edge_case(self):
        my_matrix = [[1, 2, 3],
                     [4, 5, 6],
                     [9, 8, 7]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_magic_square_edge_case2(self):
        my_matrix = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_magic_square_edge_case3(self):
        my_matrix = [[1, 2, 3],
                     [4, 5, 6],
                     [3, 2, 1]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_magic_square_edge_case4(self):
        my_matrix = [[1, 2, 3],
                     [4, 5, 6],
                     [6, 5, 4]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_magic_square_edge_case5(self):
        my_matrix = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_magic_square_edge_case6(self):
        my_matrix = [[1, 2, 3],
                     [4, 5, 6],
                     [9, 8, 7]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_magic_square_edge_case7(self):
        my_matrix = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_magic_square_edge_case8(self):
        my_matrix = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_magic_square_edge_case9(self):
        my_matrix = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_magic_square_edge_case10(self):
        my_matrix = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
        self.assertTrue(magic_square_test(my_matrix))

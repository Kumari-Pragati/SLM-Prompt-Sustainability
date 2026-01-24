import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):

    def test_typical_case(self):
        n = 3
        expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(generate_matrix(n), expected)

    def test_edge_case_n_equals_1(self):
        n = 1
        expected = [[1]]
        self.assertEqual(generate_matrix(n), expected)

    def test_boundary_case_n_equals_0(self):
        n = 0
        expected = []
        self.assertEqual(generate_matrix(n), expected)

    def test_negative_n(self):
        n = -1
        expected = []
        self.assertEqual(generate_matrix(n), expected)

    def test_large_n(self):
        n = 10
        expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    [16, 17, 18, 19, 20, 21, 22, 23, 24, 11],
                    [15, 26, 27, 28, 29, 30, 31, 32, 25, 12],
                    [14, 25, 37, 38, 39, 40, 41, 33, 32, 26],
                    [13, 24, 36, 47, 48, 49, 42, 34, 31, 27],
                    [12, 23, 35, 46, 57, 50, 43, 35, 30, 28],
                    [11, 22, 34, 45, 56, 58, 44, 36, 29, 20],
                    [10, 21, 33, 44, 55, 59, 51, 45, 37, 39],
                    [9, 19, 32, 43, 54, 60, 52, 46, 40, 42],
                    [8, 18, 31, 42, 53, 61, 53, 47, 41, 43]]
        self.assertEqual(generate_matrix(n), expected)

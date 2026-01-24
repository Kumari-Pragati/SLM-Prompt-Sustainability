import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):

    def test_typical_case(self):
        n = 3
        expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(generate_matrix(n), expected)

    def test_edge_case(self):
        n = 1
        expected = [[1]]
        self.assertEqual(generate_matrix(n), expected)

    def test_boundary_case(self):
        n = 0
        expected = []
        self.assertEqual(generate_matrix(n), expected)

    def test_negative_case(self):
        n = -1
        expected = []
        self.assertEqual(generate_matrix(n), expected)

    def test_large_case(self):
        n = 10
        expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    [16, 17, 18, 19, 20, 21, 22, 23, 24, 11],
                    [15, 26, 27, 28, 29, 30, 31, 32, 25, 12],
                    [14, 25, 36, 37, 38, 39, 40, 33, 34, 26],
                    [13, 24, 35, 46, 47, 48, 41, 32, 35, 27],
                    [12, 23, 34, 45, 49, 42, 40, 36, 30, 28],
                    [11, 22, 33, 44, 43, 37, 29, 20, 19, 17],
                    [10, 18, 29, 38, 31, 22, 13, 4, 2, 3],
                    [9, 17, 27, 36, 30, 14, 5, 1, 7, 8],
                    [8, 16, 25, 34, 28, 15, 6, 21, 1, 4]]
        self.assertEqual(generate_matrix(n), expected)

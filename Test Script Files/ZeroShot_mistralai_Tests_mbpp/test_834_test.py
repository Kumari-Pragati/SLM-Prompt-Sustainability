import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):

    def test_empty_matrix(self):
        result = generate_matrix(0)
        self.assertEqual(result, [])

    def test_1x1_matrix(self):
        result = generate_matrix(1)
        self.assertEqual(result, [[1]])

    def test_2x2_matrix(self):
        result = generate_matrix(2)
        self.assertEqual(result, [[1, 2], [4, 5]])

    def test_3x3_matrix(self):
        result = generate_matrix(3)
        self.assertEqual(result, [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    def test_4x4_matrix(self):
        result = generate_matrix(4)
        self.assertEqual(result, [[1, 2, 3, 4],
                                   [13, 14, 15, 8],
                                   [12, 11, 10, 9],
                                   [7, 6, 5, 16]])

    def test_5x5_matrix(self):
        result = generate_matrix(5)
        self.assertEqual(result, [[1, 2, 3, 4, 5],
                                   [27, 28, 29, 24, 13],
                                   [26, 25, 22, 23, 14],
                                   [21, 20, 19, 18, 15],
                                   [12, 11, 10, 9, 6]])

import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):

    def test_empty_matrix(self):
        self.assertAlmostEqual(maxAverageOfPath([[]], 0), 0)

    def test_single_row_matrix(self):
        for M in [1, 2, 3]:
            matrix = [[1] * M]
            self.assertAlmostEqual(maxAverageOfPath(matrix, M), 1)

    def test_single_column_matrix(self):
        for M in [1, 2, 3]:
            matrix = [[1] for _ in range(M)]
            self.assertAlmostEqual(maxAverageOfPath(matrix, M), 1)

    def test_square_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertAlmostEqual(maxAverageOfPath(matrix, len(matrix)), 5.0)

    def test_large_matrix(self):
        matrix = [[i + j for j in range(10)] for i in range(10)]
        self.assertAlmostEqual(maxAverageOfPath(matrix, len(matrix)), 54.5)

    def test_negative_costs(self):
        matrix = [[-1, 2], [4, -3]]
        self.assertAlmostEqual(maxAverageOfPath(matrix, len(matrix)), -0.5)

    def test_zero_costs(self):
        matrix = [[0] * 10 for _ in range(10)]
        self.assertAlmostEqual(maxAverageOfPath(matrix, len(matrix)), 0)

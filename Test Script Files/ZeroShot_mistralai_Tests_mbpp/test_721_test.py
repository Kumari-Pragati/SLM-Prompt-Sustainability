import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):

    def test_max_average_of_path(self):
        M = 100
        cost = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        N = len(cost)
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 5.0)

        cost = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 9.0)

        cost = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 12.0)

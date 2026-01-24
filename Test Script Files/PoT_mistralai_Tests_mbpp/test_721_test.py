import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):

    def test_typical_case(self):
        cost = [
            [1, 3, 5],
            [2, 4, 6],
            [7, 8, 9]
        ]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 5.0)

    def test_edge_case_empty(self):
        cost = []
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 0.0)

    def test_edge_case_single_row(self):
        cost = [[1]]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 1.0)

    def test_edge_case_single_column(self):
        cost = [[1]] * 3
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost[0])), 1.0)

    def test_corner_case_diagonal(self):
        cost = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 5.0)

    def test_corner_case_reverse_diagonal(self):
        cost = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 5.0)

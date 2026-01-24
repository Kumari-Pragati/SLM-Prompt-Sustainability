import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):

    def test_simple_input(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 4.5)

    def test_edge_input(self):
        cost = [[0], [0]]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 0.0)
        cost = [[1000000000], [1000000000]]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 1000000000.0)

    def test_boundary_input(self):
        cost = [[0, 0], [0, 1]]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 0.5)
        cost = [[1, 2, 3, 4], [5, 6, 7, 8]]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 5.0)

    def test_complex_input(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 5.5)
        cost = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 12.0)

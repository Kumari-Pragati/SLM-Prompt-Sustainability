import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):
    def test_typical_case(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 5.0)

    def test_boundary_case_1x1(self):
        cost = [[1]]
        N = 1
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 1.0)

    def test_boundary_case_empty(self):
        cost = []
        N = 0
        with self.assertRaises(IndexError):
            maxAverageOfPath(cost, N)

    def test_edge_case_large_N(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 100
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 5.0)

    def test_invalid_input_negative_cost(self):
        cost = [[-1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        with self.assertRaises(ValueError):
            maxAverageOfPath(cost, N)

    def test_invalid_input_non_integer_cost(self):
        cost = [['1', 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        with self.assertRaises(TypeError):
            maxAverageOfPath(cost, N)

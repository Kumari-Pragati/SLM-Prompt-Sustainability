import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):
    def test_typical_use_case(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 5.0)

    def test_edge_case_N_1(self):
        cost = [[1]]
        N = 1
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 1.0)

    def test_edge_case_N_100(self):
        cost = [[i for i in range(1, 101)] for _ in range(1, 101)]
        N = 100
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 50.5)

    def test_invalid_input_N_0(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 0
        with self.assertRaises(ValueError):
            maxAverageOfPath(cost, N)

    def test_invalid_input_cost_empty(self):
        cost = []
        N = 100
        with self.assertRaises(ValueError):
            maxAverageOfPath(cost, N)

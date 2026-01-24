import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):

    def test_typical_case(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 5.0)

    def test_edge_case_single_element(self):
        cost = [[1]]
        N = 1
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 1.0)

    def test_boundary_case_empty_matrix(self):
        cost = []
        N = 0
        self.assertEqual(maxAverageOfPath(cost, N), 0)

    def test_corner_case_negative_numbers(self):
        cost = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        N = 3
        self.assertAlmostEqual(maxAverageOfPath(cost, N), -5.0)

    def test_corner_case_large_numbers(self):
        cost = [[1000, 2000, 3000], [4000, 5000, 6000], [7000, 8000, 9000]]
        N = 3
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 5000.0)

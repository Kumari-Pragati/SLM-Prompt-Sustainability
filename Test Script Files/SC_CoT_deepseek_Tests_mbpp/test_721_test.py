import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):

    def test_typical_case(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 5.0)

    def test_edge_case_N_equals_1(self):
        cost = [[1]]
        N = 1
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 1.0)

    def test_edge_case_N_equals_2(self):
        cost = [[1, 2], [3, 4]]
        N = 2
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 2.5)

    def test_boundary_case_N_equals_0(self):
        cost = []
        N = 0
        self.assertEqual(maxAverageOfPath(cost, N), 0)

    def test_invalid_input_N_greater_than_cost_length(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 4
        with self.assertRaises(IndexError):
            maxAverageOfPath(cost, N)

    def test_invalid_input_cost_not_a_list(self):
        cost = "not a list"
        N = 3
        with self.assertRaises(TypeError):
            maxAverageOfPath(cost, N)

    def test_invalid_input_N_not_an_integer(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = "not an integer"
        with self.assertRaises(TypeError):
            maxAverageOfPath(cost, N)

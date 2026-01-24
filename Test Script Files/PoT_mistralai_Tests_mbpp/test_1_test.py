import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):
    def test_typical_case(self):
        cost = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(min_cost(cost, len(cost), len(cost[0])), 6)

    def test_edge_case_small_matrix(self):
        cost = [
            [1]
        ]
        self.assertEqual(min_cost(cost, len(cost), len(cost[0])), 1)

    def test_edge_case_empty_matrix(self):
        cost = []
        self.assertEqual(min_cost(cost, len(cost), len(cost[0])), 0)

    def test_edge_case_single_row(self):
        cost = [
            [1, 2, 3]
        ]
        self.assertEqual(min_cost(cost, len(cost), len(cost[0])), 1)

    def test_edge_case_single_column(self):
        cost = [
            [1]
        ]
        self.assertEqual(min_cost(cost, len(cost), len(cost[0])), 1)

    def test_corner_case_diagonal(self):
        cost = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(min_cost(cost, len(cost), len(cost[0])), 6)

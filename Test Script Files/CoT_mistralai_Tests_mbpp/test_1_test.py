import unittest
from1_code import min_cost

class TestMinCost(unittest.TestCase):
    def test_typical_case(self):
        cost = [
            [1, 3, 5],
            [8, 3, 4],
            [9, 2, 6]
        ]
        m, n = len(cost), len(cost[0])
        self.assertEqual(min_cost(cost, m, n), 7)

    def test_edge_case_1(self):
        cost = [
            [1],
            [2]
        ]
        m, n = len(cost), len(cost[0])
        self.assertEqual(min_cost(cost, m, n), 1)

    def test_edge_case_2(self):
        cost = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        m, n = len(cost), len(cost[0])
        self.assertEqual(min_cost(cost, m, n), 6)

    def test_edge_case_3(self):
        cost = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        m, n = len(cost), len(cost[0])
        self.assertEqual(min_cost(cost, m, n), 10)

    def test_invalid_input_1(self):
        with self.assertRaises(ValueError):
            min_cost([], 0, 0)

    def test_invalid_input_2(self):
        with self.assertRaises(ValueError):
            min_cost([[1]], 0, -1)

    def test_invalid_input_3(self):
        with self.assertRaises(ValueError):
            min_cost([[1]], -1, 0)

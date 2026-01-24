import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):
    def test_valid_input(self):
        cost = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(min_cost(cost, len(cost), len(cost[0])), 11)

    def test_empty_input(self):
        cost = []
        with self.assertRaises(ValueError):
            min_cost(cost, 0, 0)

    def test_single_row_input(self):
        cost = [
            [1]
        ]
        self.assertEqual(min_cost(cost, 1, 1), 1)

    def test_single_column_input(self):
        cost = [
            [1]
        ]
        self.assertEqual(min_cost(cost, 1, len(cost)), 1)

    def test_negative_input(self):
        cost = [
            [-1, -2, -3],
            [-4, -5, -6],
            [-7, -8, -9]
        ]
        with self.assertRaises(ValueError):
            min_cost(cost, len(cost), len(cost[0]))

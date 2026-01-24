import unittest
from1_code import min_cost

class TestMinCost(unittest.TestCase):

    def test_valid_input(self):
        cost = [
            [1, 3, 5],
            [8, 6, 7],
            [9, 2, 4]
        ]
        self.assertEqual(min_cost(cost, 3, 3), 11)

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

    def test_zero_row_input(self):
        cost = [
            []
        ]
        with self.assertRaises(ValueError):
            min_cost(cost, 0, 0)

    def test_zero_column_input(self):
        cost = [
            [0]
        ]
        with self.assertRaises(ValueError):
            min_cost(cost, len(cost), 0)

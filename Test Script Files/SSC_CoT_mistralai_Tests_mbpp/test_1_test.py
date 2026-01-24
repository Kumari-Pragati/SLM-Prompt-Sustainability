import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):

    def test_normal_case(self):
        cost = [
            [1, 3, 5],
            [8, 6, 7],
            [9, 2, 4]
        ]
        self.assertEqual(min_cost(cost, 3, 3), 11)

    def test_edge_case_small_matrix(self):
        cost = [
            [1],
            [2]
        ]
        self.assertEqual(min_cost(cost, 2, 1), 3)

    def test_edge_case_empty_matrix(self):
        cost = []
        self.assertEqual(min_cost(cost, 0, 0), 0)

    def test_edge_case_single_row(self):
        cost = [
            [1, 3, 5]
        ]
        self.assertEqual(min_cost(cost, 1, 3), 8)

    def test_edge_case_single_column(self):
        cost = [
            [1, 8],
            [2, 6]
        ]
        self.assertEqual(min_cost(cost, 2, 1), 10)

    def test_invalid_input_negative_dimensions(self):
        with self.assertRaises(ValueError):
            min_cost(cost, -1, 3)

    def test_invalid_input_zero_dimensions(self):
        with self.assertRaises(ValueError):
            min_cost(cost, 0, 0)

import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):

    def test_typical_case(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        self.assertEqual(min_cost(cost, 2, 2), 8)

    def test_edge_case_single_row(self):
        cost = [[1, 2, 3]]
        self.assertEqual(min_cost(cost, 0, 2), 6)

    def test_edge_case_single_column(self):
        cost = [[1], [2], [3]]
        self.assertEqual(min_cost(cost, 2, 0), 6)

    def test_boundary_case_empty_matrix(self):
        cost = [[], []]
        self.assertEqual(min_cost(cost, 0, 0), 0)

    def test_corner_case_all_same_values(self):
        cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(min_cost(cost, 2, 2), 3)

    def test_corner_case_all_different_values(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_cost(cost, 2, 2), 15)

    def test_invalid_input_negative_cost(self):
        cost = [[-1, 2, 3], [4, -5, 2], [1, 5, 3]]
        with self.assertRaises(ValueError):
            min_cost(cost, 2, 2)

    def test_invalid_input_non_integer_cost(self):
        cost = [['1', 2, 3], [4, '5', 2], [1, 5, 3]]
        with self.assertRaises(TypeError):
            min_cost(cost, 2, 2)

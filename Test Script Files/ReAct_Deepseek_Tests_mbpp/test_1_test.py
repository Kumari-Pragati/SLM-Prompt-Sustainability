import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):

    def test_typical_case(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        m = 2
        n = 2
        expected_output = 8
        self.assertEqual(min_cost(cost, m, n), expected_output)

    def test_edge_case_single_cell(self):
        cost = [[1]]
        m = 0
        n = 0
        expected_output = 1
        self.assertEqual(min_cost(cost, m, n), expected_output)

    def test_edge_case_empty_matrix(self):
        cost = [[], []]
        m = -1
        n = -1
        expected_output = 0
        self.assertEqual(min_cost(cost, m, n), expected_output)

    def test_error_case_negative_cost(self):
        cost = [[-1, 2, 3], [4, 8, 2], [1, 5, 3]]
        m = 2
        n = 2
        with self.assertRaises(ValueError):
            min_cost(cost, m, n)

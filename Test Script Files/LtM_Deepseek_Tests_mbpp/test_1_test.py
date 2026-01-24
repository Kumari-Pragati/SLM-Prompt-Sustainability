import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):

    def test_simple_input(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        self.assertEqual(min_cost(cost, 2, 2), 8)

    def test_edge_conditions(self):
        # Test with empty cost matrix
        self.assertEqual(min_cost([[]], 0, 0), 0)
        # Test with single element cost matrix
        self.assertEqual(min_cost([[1]], 0, 0), 1)
        # Test with cost matrix of all zeros
        self.assertEqual(min_cost([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 2, 2), 0)

    def test_boundary_conditions(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        # Test with m=0
        self.assertEqual(min_cost(cost, 0, 2), 2)
        # Test with n=0
        self.assertEqual(min_cost(cost, 2, 0), 1)
        # Test with m=n=0
        self.assertEqual(min_cost([[0]], 0, 0), 0)

    def test_complex_cases(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        # Test with maximum values
        self.assertEqual(min_cost(cost, 2, 2), 8)
        # Test with minimum values
        self.assertEqual(min_cost([[1, 2, 3], [4, 1, 2], [1, 5, 1]], 2, 2), 2)
        # Test with negative values
        self.assertEqual(min_cost([[-1, -2, -3], [-4, -8, -2], [-1, -5, -3]], 2, 2), -2)

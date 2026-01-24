import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):
    def test_typical_case(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        m = 2
        n = 2
        self.assertEqual(min_cost(cost, m, n), 7)

    def test_boundary_case(self):
        cost = [[1]]
        m = 0
        n = 0
        self.assertEqual(min_cost(cost, m, n), 1)

    def test_edge_case(self):
        cost = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        m = 2
        n = 2
        self.assertEqual(min_cost(cost, m, n), 0)

    def test_invalid_input(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        m = -1
        n = 2
        with self.assertRaises(Exception):
            min_cost(cost, m, n)

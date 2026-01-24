import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):

    def test_min_cost_empty(self):
        cost = []
        m, n = 0, 0
        self.assertEqual(min_cost(cost, m, n), 0)

    def test_min_cost_single_row(self):
        cost = [[1]]
        m, n = 1, 1
        self.assertEqual(min_cost(cost, m, n), 1)

    def test_min_cost_single_column(self):
        cost = [[1]]
        m, n = 1, 3
        self.assertEqual(min_cost(cost, m, n), 3)

    def test_min_cost_2x2(self):
        cost = [[1, 2], [3, 4]]
        m, n = 2, 2
        self.assertEqual(min_cost(cost, m, n), 3)

    def test_min_cost_3x3(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m, n = 3, 3
        self.assertEqual(min_cost(cost, m, n), 6)

    def test_min_cost_with_zero(self):
        cost = [[0, 1], [2, 0]]
        m, n = 2, 2
        self.assertEqual(min_cost(cost, m, n), 1)

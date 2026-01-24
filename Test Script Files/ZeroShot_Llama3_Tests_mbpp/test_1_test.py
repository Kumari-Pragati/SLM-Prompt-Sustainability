import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):

    def test_min_cost(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_cost(cost, 3, 3), 12)

    def test_min_cost_edge_case1(self):
        cost = [[1]]
        self.assertEqual(min_cost(cost, 1, 1), 1)

    def test_min_cost_edge_case2(self):
        cost = [[1, 2]]
        self.assertEqual(min_cost(cost, 1, 2), 3)

    def test_min_cost_edge_case3(self):
        cost = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(min_cost(cost, 2, 3), 9)

    def test_min_cost_edge_case4(self):
        cost = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertEqual(min_cost(cost, 1, 9), 28)

    def test_min_cost_edge_case5(self):
        cost = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]
        self.assertEqual(min_cost(cost, 1, 30), 465)

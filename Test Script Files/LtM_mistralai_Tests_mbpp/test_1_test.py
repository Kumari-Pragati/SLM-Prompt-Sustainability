import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):

    def test_simple(self):
        cost = [[1, 2], [3, 4]]
        self.assertEqual(min_cost(cost, 2, 2), 7)

    def test_edge_and_boundary(self):
        cost = [[1], [2]]
        self.assertEqual(min_cost(cost, 1, 2), 3)
        cost = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(min_cost(cost, 3, 2), 15)
        cost = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(min_cost(cost, 2, 3), 17)

    def test_complex(self):
        cost = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.assertEqual(min_cost(cost, 4, 4), 85)
        cost = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
        self.assertEqual(min_cost(cost, 5, 5), 205)

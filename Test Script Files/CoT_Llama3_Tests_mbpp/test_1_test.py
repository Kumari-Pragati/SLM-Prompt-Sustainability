import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):
    def test_min_cost(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_cost(cost, 3, 3), 12)

        cost = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(min_cost(cost, 2, 3), 6)

        cost = [[1, 2, 3]]
        self.assertEqual(min_cost(cost, 1, 3), 3)

        cost = [[1, 2]]
        self.assertEqual(min_cost(cost, 1, 2), 3)

        cost = [[1]]
        self.assertEqual(min_cost(cost, 1, 1), 1)

        cost = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertEqual(min_cost(cost, 1, 9), 28)

        cost = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
        self.assertEqual(min_cost(cost, 1, 20), 66)

        cost = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]
        self.assertEqual(min_cost(cost, 1, 30), 93)

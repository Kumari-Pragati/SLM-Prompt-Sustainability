import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):

    def test_typical_case(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        m = 2
        n = 2
        self.assertEqual(min_cost(cost, m, n), 8)

    def test_single_element(self):
        cost = [[1]]
        m = 0
        n = 0
        self.assertEqual(min_cost(cost, m, n), 1)

    def test_empty_cost(self):
        cost = []
        m = -1
        n = -1
        self.assertEqual(min_cost(cost, m, n), 0)

    def test_negative_cost(self):
        cost = [[-1, -2, -3], [-4, -8, -2], [-1, -5, -3]]
        m = 2
        n = 2
        self.assertEqual(min_cost(cost, m, n), -8)

    def test_large_cost(self):
        cost = [[1000, 2000, 3000], [4000, 8000, 2000], [1000, 5000, 3000]]
        m = 2
        n = 2
        self.assertEqual(min_cost(cost, m, n), 2000)

    def test_boundary_case(self):
        cost = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        m = 2
        n = 1
        self.assertEqual(min_cost(cost, m, n), 0)

    def test_invalid_input(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        m = -1
        n = 2
        with self.assertRaises(ValueError):
            min_cost(cost, m, n)

import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):

    def test_min_cost(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        m = 2
        n = 2
        expected_output = 8
        self.assertEqual(min_cost(cost, m, n), expected_output)

    def test_min_cost_with_zeroes(self):
        cost = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        m = 2
        n = 2
        expected_output = 0
        self.assertEqual(min_cost(cost, m, n), expected_output)

    def test_min_cost_with_negative_numbers(self):
        cost = [[-1, -2, -3], [-4, -8, -2], [-1, -5, -3]]
        m = 2
        n = 2
        expected_output = -4
        self.assertEqual(min_cost(cost, m, n), expected_output)

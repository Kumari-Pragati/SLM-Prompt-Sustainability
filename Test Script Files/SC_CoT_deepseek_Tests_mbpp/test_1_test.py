import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):

    def test_typical_case(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        m = 2
        n = 2
        self.assertEqual(min_cost(cost, m, n), 8)

    def test_edge_case_m_0(self):
        cost = [[1, 2, 3]]
        m = 0
        n = 2
        self.assertEqual(min_cost(cost, m, n), cost[0][0])

    def test_edge_case_n_0(self):
        cost = [[1], [2], [3]]
        m = 2
        n = 0
        self.assertEqual(min_cost(cost, m, n), cost[0][0])

    def test_edge_case_m_n_0(self):
        cost = [[1]]
        m = 0
        n = 0
        self.assertEqual(min_cost(cost, m, n), cost[0][0])

    def test_corner_case_all_same(self):
        cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        m = 2
        n = 2
        self.assertEqual(min_cost(cost, m, n), 3)

    def test_invalid_input_m_negative(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        m = -1
        n = 2
        with self.assertRaises(Exception):
            min_cost(cost, m, n)

    def test_invalid_input_n_negative(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        m = 2
        n = -1
        with self.assertRaises(Exception):
            min_cost(cost, m, n)

    def test_invalid_input_m_not_int(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        m = 'two'
        n = 2
        with self.assertRaises(Exception):
            min_cost(cost, m, n)

    def test_invalid_input_n_not_int(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        m = 2
        n = 'two'
        with self.assertRaises(Exception):
            min_cost(cost, m, n)

import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):

    def test_typical_case(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_cost(cost, 3, 3), 18)

    def test_edge_case_m_zero(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_cost(cost, 0, 3), 1)

    def test_edge_case_n_zero(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_cost(cost, 3, 0), 1)

    def test_edge_case_m_n_zero(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_cost(cost, 0, 0), 0)

    def test_error_case_invalid_m(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(IndexError):
            min_cost(cost, -1, 3)

    def test_error_case_invalid_n(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(IndexError):
            min_cost(cost, 3, -1)

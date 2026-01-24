import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):
    def test_typical_input(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_cost(cost, 3, 3), 28)

    def test_edge_case_m_zero(self):
        cost = [[1, 2, 3]]
        self.assertEqual(min_cost(cost, 1, 3), 6)

    def test_edge_case_n_zero(self):
        cost = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertEqual(min_cost(cost, 3, 0), 6)

    def test_edge_case_m_n_zero(self):
        cost = [[1]]
        self.assertEqual(min_cost(cost, 1, 0), 1)

    def test_invalid_input_m_negative(self):
        cost = [[1, 2, 3]]
        with self.assertRaises(IndexError):
            min_cost(cost, -1, 3)

    def test_invalid_input_n_negative(self):
        cost = [[1, 2, 3]]
        with self.assertRaises(IndexError):
            min_cost(cost, 3, -1)

    def test_invalid_input_m_zero_n_zero(self):
        cost = [[1, 2, 3]]
        with self.assertRaises(IndexError):
            min_cost(cost, 0, 0)
